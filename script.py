import boto3
import yaml
import os

myclient = boto3.client('s3')

with open('cf.yml','r') as f:
    mydata = yaml.safe_load(f)

bucket_name = os.environ['BucketName']
awsregion = os.environ['AwsRegionBucket']
if(bucket_name == None):
    bucket_name = mydata['BucketName']

# location = config.get('Location','us-east-2')
myclient.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':awsregion},)








