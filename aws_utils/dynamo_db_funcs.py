import boto3
from utils.read_files import yaml_data
from datetime import datetime
import pandas as pd
import uuid

#from pyspark.sql.functions import col
#from pyspark.sql import SparkSession


def get_popular_spark():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("DynamoDB Spark Example") \
        .getOrCreate()
    # Read data from DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name=yaml_data['region_name'],
                              aws_access_key_id=yaml_data['aws_access_key_id'],
                              aws_secret_access_key=yaml_data['aws_secret_access_key'])
    table = dynamodb.Table(yaml_data['table_name'])
    response = table.scan()

    # Create Spark DataFrame from DynamoDB data
    data = response['Items']
    df = spark.createDataFrame(data)

    # Perform Spark operations
    value_counts = df.groupBy("id").count()

    # Order the result in descending order of count and retrieve the top 10
    top_10_values = value_counts.orderBy(col("count").desc()).limit(10)

    top_10_values_list = [row['id'] for row in top_10_values.collect()]
    lst = []

    for row in top_10_values_list:
        lst.append(int(row))
    print(lst)

    # Stop Spark session
    spark.stop()
    return lst


def get_popular():
    # Read data from DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name=yaml_data['region_name'],
                              aws_access_key_id=yaml_data['aws_access_key_id'],
                              aws_secret_access_key=yaml_data['aws_secret_access_key'])
    table = dynamodb.Table(yaml_data['table_name'])
    response = table.scan()
    items = response['Items']

    # Convert to Pandas DataFrame
    df = pd.DataFrame(items)
    value_counts = df['id'].value_counts()
    print(value_counts)

    # Get the top 10 most frequent values
    top_10_values = value_counts.head(10)
    top_10_values =top_10_values.index.tolist()
    return [int(value) for value in top_10_values]


def insert_event_to_dynamodb(new_item_data):
    # Set up DynamoDB resource and table
    dynamodb = boto3.resource('dynamodb', region_name=yaml_data['region_name'],
                              aws_access_key_id=yaml_data['aws_access_key_id'],
                              aws_secret_access_key=yaml_data['aws_secret_access_key'])
    table_name = yaml_data['table_name']
    new_item_data["date"] = str(datetime.now().date())
    new_item_data["key"] = str(uuid.uuid4())
    table = dynamodb.Table(table_name)
    table.put_item(Item=new_item_data)

    print("data successfully uploaded to DynamoDB.")
    return True


if __name__ == '__main__':
    get_popular()
