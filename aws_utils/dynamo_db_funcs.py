import boto3
from utils.read_files import yaml_data
from datetime import datetime


def insert_event_to_dynamodb(new_item_data):
    # Set up DynamoDB resource and table
    dynamodb = boto3.resource('dynamodb', region_name=yaml_data['region_name'],
                              aws_access_key_id=yaml_data['aws_access_key_id'],
                              aws_secret_access_key=yaml_data['aws_secret_access_key'])
    table_name = yaml_data['table_name']
    new_item_data["date"] = str(datetime.now().date())
    table = dynamodb.Table(table_name)
    table.put_item(Item=new_item_data)

    print("CSV data successfully uploaded to DynamoDB.")


if __name__ == '__main__':
    insert_event_to_dynamodb({'id': 3, "time": "jdik"})
