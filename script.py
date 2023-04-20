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



policy = '''{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "arn:aws:iam::268819417241:role/accessS3UsingEc2",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:PutObjectAcl" 
            ],
            "Resource": [
                "arn:aws:s3:::%s/*"
            ]
        }
    ]
}''' % bucket_name

myclient.put_bucket_policy(Bucket=bucket_name, Policy=policy)







