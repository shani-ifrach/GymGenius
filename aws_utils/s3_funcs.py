import boto3
import pandas as pd
from io import StringIO
import os
from utils.read_files import yaml_data


def upload_file_to_s3(file):
    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=yaml_data['aws_access_key_id'], aws_secret_access_key=yaml_data['aws_secret_access_key'], region_name=yaml_data['region_name'])
    s3_key = os.path.basename(file)
    # Upload the local file to S3
    s3.upload_file(file, yaml_data['s3_bucket_name'], s3_key)

    print(f"File uploaded to S3 bucket: {yaml_data['s3_bucket_name']}, Key: {s3_key}")


def update_csv_in_s3(new_data, s3_key):
    # new data is dataframe
    s3_client = boto3.client('s3', aws_access_key_id=yaml_data['aws_access_key_id'], aws_secret_access_key=yaml_data['aws_secret_access_key'], region_name=yaml_data['region_name'])
    response = s3_client.get_object(Bucket=yaml_data['s3_bucket_name'], Key=s3_key)
    existing_content = response['Body'].read().decode('utf-8')

    # Read existing CSV into a Pandas DataFrame
    existing_data = pd.read_csv(StringIO(existing_content))

    # Append new data to the existing DataFrame
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)

    # Convert the updated DataFrame to a CSV string
    updated_content = updated_data.to_csv(index=False)

    # Upload the updated content back to S3
    s3_client.put_object(Bucket=yaml_data['s3_bucket_name'], Key=s3_key, Body=updated_content.encode('utf-8'))

    print("CSV file updated successfully.")


if __name__ == '__main__':
    #upload_file_to_s3()
    upload_file_to_s3(r"C:\Users\LIRAZ\PycharmProjects\GymGenius\utils\params.yml")