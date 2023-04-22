import boto3
import yaml
import os

# Create a CloudFormation client
cf_client = boto3.client('cloudformation',region_name='us-east-2')
template_body = open('ec2.yml', 'r').read()
# Create the stack
response = cf_client.create_stack(
    StackName='EC2inaccount2',
    TemplateBody=template_body,
    Parameters=[
        {
            'ParameterKey': 'InstanceName',
            'ParameterValue': os.environ['InstanceName']
        },
        {
            'ParameterKey': 'InstanceType',
            'ParameterValue': os.environ['InstanceType']
        },
        {
            'ParameterKey': 'BucketName',
            'ParameterValue': os.environ['BucketName']
        },
        {
            'ParameterKey': 'IamUsername',
            'ParameterValue': os.environ['IamUsername']
        }
    ],
    Capabilities=['CAPABILITY_IAM','CAPABILITY_AUTO_EXPAND','CAPABILITY_NAMED_IAM']
)

print(response)
