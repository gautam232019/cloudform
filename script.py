import boto3
import yaml

myclient = boto3.client('s3')

with open('cf.yml','r') as f:
    mydata = yaml.load(f,Loader=yaml.FullLoader)

bucket_name = mydata['BucketName']
# location = config.get('Location','us-east-2')
myclient.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':'us-east-2'},)








