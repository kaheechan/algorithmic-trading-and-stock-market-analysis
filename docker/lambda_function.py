import json as js
import boto3 as bt
import pandas as pd
import yfinance as yf
import os
import urllib.parse
import smtplib as sl
from io import StringIO
from datetime import datetime as dt
from sqlalchemy import create_engine as ce

def stock_data(ticker: str, mode: str)-> pd.DataFrame:
    start_date = '2021-01-01'
    end_date = dt.now().strftime('%Y-%m-%d')

    if mode == 'replace':
        stock_df = yf.download(ticker, start=start_date, end=end_date, interval='1d')
        dividends_df = yf.Ticker(ticker).dividends.to_frame().loc[start_date:end_date]
        stock_df = stock_df.join(dividends_df, on='date', how='left')
        stock_df['Dividends'].fillna(0, inplace=True)

    elif mode == 'append':
        stock_df = yf.Ticker(ticker).history(period='1d')

        if 'Dividends' not in stock_df.columns:
            stock_df['Dividends'] = 0

        stock_df = stock_df[['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends']]

    else:
        raise ValueError(f"Please make sure that your mode is either append or replace: mode, {mode}. \n")

    stock_df.index.name = 'date'

    return stock_df

def stock_name(event: dict) -> str:
    # Get the s3 bucket and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Initialize s3 client
    s3 = bt.client('s3')

    # Get the CSV File Content from s3
    csv_file = s3.get_object(Bucket=bucket_name, Key=object_key)
    csv_content = csv_file['Body'].read().decode('utf-8')

    # Read the CSV File
    df = pd.read_csv(StringIO(csv_content))

    # Return the ticker name
    return df['ticker'].iloc[0]

def stock_db(stock_df: pd.DataFrame, mode: str):
    try:
        # Retrieve environment variables
        db_host = os.getenv('DB_HOST', 'default_host')
        db_name = os.getenv('DB_NAME', 'default_db')
        db_user = os.getenv('DB_USER', 'default_user')
        db_password = os.getenv('DB_PASSWORD', 'default_password')

        # URL encode the password to handle special characters
        db_password = urllib.parse.quote_plus(db_password)

        # Create the connection string
        connection = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}"

        # Print connection string for debugging purposes
        print(f"Connecting to database using: {connection}")

        # Create the SQLAlchemy engine
        engine = ce(connection)

        # Write the DataFrame to the database
        if mode == 'replace':
            stock_df.to_sql('stock_data', engine, if_exists='replace', index=True, index_label='date')
            print("DataFrame replacing database successfully")

        elif mode == 'append':
            stock_df.to_sql('stock_data', engine, if_exists='append', index=True, index_label='date')
            print("DataFrame appending to database successfully")

        else:
            raise ValueError(f"Please make sure that your mode is either append or replace: mode, {mode}. \n")



    except Exception as e:
        print(f"Failed to write DataFrame to database: {e}")

def send_email(ticker: str):
    try:
        email_name = os.getenv('EMAIL_NAME', 'default_email_name')
        email_password = os.getenv('EMAIL_PASSWORD', 'default_email_password')
        email_recipient = os.getenv('EMAIL_RECIPIENT', 'default_email_recipient')
        email_server = os.getenv('EMAIL_SERVER', 'default_server')
        email_port = int(os.getenv('EMAIL_PORT', 'default_port'))

        email_subject = f"""Stock Data Update: {dt.now().strftime('%Y-%m-%d %I:%M')}"""
        email_body = f"""Dear, \n\n Ticker name: {ticker} data was updated. \n\n Best,\n Kahee"""
        email_message = f"Subject: {email_subject}\n\n{email_body}"

        with sl.SMTP(email_server, email_port) as smtp:
            smtp.starttls()
            smtp.login(email_name, email_password)
            smtp.sendmail(email_name, email_recipient, email_message)

        print(f"Email sending to recipient {email_recipient} successfully")

    except Exception as e:
        print(f"Failed to send Email to Recipient: {e}")

def lambda_handler(event, context):
    mode = 'append'

    # Get ticker name
    ticker = stock_name(event)

    # Download Data
    stock_df = stock_data(ticker, mode)

    # Save to Database
    stock_db(stock_df, mode)

    # Send an Email
    send_email(ticker)

    # Return
    return {
        'statusCode': 200,
        'body': js.dumps('DB processed successfully!')
    }