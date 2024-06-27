import upload as ul

if __name__ == '__main__':
    tickers = ['SPY']
    access_key = 'AKIAQ3EGRD5MAWPPCNH5'
    secret_key = '' \
                 ''
    bucket_name = 'automation-python-01'
    s3_name = 'tickers.csv'

    file_name = ul.create_csv(tickers)
    ul.upload_csv(access_key, secret_key, bucket_name, s3_name, file_name)


