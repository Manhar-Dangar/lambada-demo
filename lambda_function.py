import pandas as pd
import boto3

def lambda_handler(event, context):
    print('APP version 1.3')


client = boto3.client('dynamodb')

def handler(event, context):
  data = client.put_item(
    TableName='stud',
    Item={
        'studeName': {
          'S': 'Rohan'
        },
        'studCourse': {
          'S': 'Mcom'
        }
    }
  )

  response = {
      'statusCode': 200,
      'body': 'successfully created item!',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response