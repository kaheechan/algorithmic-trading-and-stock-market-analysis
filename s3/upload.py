import boto3 as bt
import pandas as pd

def create_csv(tickers: list) -> str:
    data = {'ticker': tickers}
    df = pd.DataFrame(data)
    df.to_csv("tickers.csv", index=False)
    return "tickers.csv"

def upload_csv(access_key: str, secret_key: str, bucket_name: str, s3_name: str, file_name: str):
    s3 = bt.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    try:
        s3.upload_file(file_name, bucket_name, s3_name)
        print("Upload Successful")

    except FileNotFoundError:
        print("The file was not found")

    except Exception as e:
        print(f"An Error Occurred, {e}")
