import boto3
import yaml
import os

# Create a CloudFormation client
cf_client = boto3.client('cloudformation',region_name='us-east-2')

# Create the stack
response = cf_client.create_stack(
    StackName='EC2inaccount2',
    TemplateBody='file://ec2.yaml',
    Parameters=[
        {
            'ParameterKey': 'InstanceName',
            'ParameterValue': os.environ['InstanceName']
        },
        {
            'ParameterKey': 'InstanceType',
            'ParameterValue': os.environ['InstanceType']
        }
    ]
)

print(response)
