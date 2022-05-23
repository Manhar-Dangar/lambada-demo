import pandas as pd
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.client('stud')
    
    dynamodb.put_item(TableName='stud', Item={'studeName':{'S':'Rohan'},'studCourse':{'S':'Mtech'}})

    print('Hello version 5')
    
