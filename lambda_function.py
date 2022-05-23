import pandas as pd
import boto3

def lambda_handler(event, context):
    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')


client = boto3.client('dynamodb')

def handler(event, context):
  data = client.put_item(
    TableName='stud',
    Item={
        'studeName': {
          'S': 'Rahul'
        },
        'studCourse': {
          'S': 'MCA'
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