# Import the SDK
# Environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY)
import boto3
import pandas as pd
import numpy as np
import os

s3client = boto3.client('s3')

print("starting job..")

bucket = os.environ['BUCKET']
object_name = os.environ['OBJECT']

s3client.download_file(bucket, object_name, '/tmp/data.csv')

df = open("/tmp/data.csv", "r")
data = pd.DataFrame(df)

# count the number of missing values for each column
mask = data.isna().sum()
#the ratio of missing values of each column
mask2 = data.isna().sum()/len(data)
print(mask)
print(mask2)
      
# drop all rows with any NaN and NaT values
df1 = data.dropna()
print(data)
