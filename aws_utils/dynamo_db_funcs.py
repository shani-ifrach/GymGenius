import boto3
from utils.read_files import yaml_data
from datetime import datetime

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc


def get_favorites():
    return None

def spark():
    spark = SparkSession.builder.appName("DynamoDBAnalysis").config("spark.hadoop.fs.s3a.access.key", yaml_data['aws_access_key_id']) \
                    .config("spark.hadoop.fs.s3a.secret.key", yaml_data['aws_secret_access_key']).getOrCreate()

    # Read data from DynamoDB
    dynamodb_df = spark.read.format("dynamodb").option("region", yaml_data['region_name']).option("table",
                                                                                       yaml_data['table_name']).load()

    # Count occurrences of each value
    value_counts = dynamodb_df.groupBy("id").count()

    # Get the top 10 values
    top_values = value_counts.orderBy(desc("count")).limit(10)

    # Create a new DynamoDB table with the top values
    # (You may need to use a DynamoDB client library like boto3 for this)
    # ...

    # Stop the Spark session
    spark.stop()


def insert_event_to_dynamodb(new_item_data):
    print(new_item_data)

    # Set up DynamoDB resource and table
    dynamodb = boto3.resource('dynamodb', region_name=yaml_data['region_name'],
                              aws_access_key_id=yaml_data['aws_access_key_id'],
                              aws_secret_access_key=yaml_data['aws_secret_access_key'])
    table_name = yaml_data['table_name']
    new_item_data["date"] = str(datetime.now().date()) + "9"
    table = dynamodb.Table(table_name)
    table.put_item(Item=new_item_data)

    print("CSV data successfully uploaded to DynamoDB.")
    return True


if __name__ == '__main__':
    #insert_event_to_dynamodb({'id': 4, "time": "jdik"})
    spark()