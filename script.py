import boto3
import yaml
import os

# Create a CloudFormation client
cf_client = boto3.client('cloudformation',region_name='us-east-2')

# Create the stack
response = cf_client.create_stack(
    StackName='S3_in_account_1',
    TemplateBody='file://cf.yml',
    Parameters=[
        {
            'ParameterKey': 'BucketName',
            'ParameterValue': os.environ['BucketName']
        },
    ]
)

