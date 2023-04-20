import boto3
import yaml
import os

# Load the parameters from the YAML file
with open('cf.yml', 'r') as f:
    parameters = yaml.safe_load(f)['Parameters']

# Create a CloudFormation client
cf_client = boto3.client('cloudformation')

# Create the stack
response = cf_client.create_stack(
    StackName='S3_in_account_1',
    TemplateBody='file://cf.yml',
    Parameters=[
        {
            'ParameterKey': key,
            'ParameterValue': os.environ[key]
        }
        for key in parameters.items()
    ]
)

