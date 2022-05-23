import pandas as pd
import boto3

client = boto3.client('dynamodb')

def handler(event, context):
  data = client.put_item(
    TableName='stud',
    Item={
        'studeName': {
          'S': 'Manhar'
        },
        'studCourse': {
          'S': 'RM'
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