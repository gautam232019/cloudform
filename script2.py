import boto3
import yaml
import os

# Load the parameters from the YAML file
with open('ec2.yml', 'r') as f:
    parameters = yaml.safe_load(f)['Parameters']

# Create a CloudFormation client
cf_client = boto3.client('cloudformation')

# Create the stack
response = cf_client.create_stack(
    StackName='EC2_in_account2',
    TemplateBody='file://ec2.yaml',
    Parameters=[
        {
            'ParameterKey': key,
            'ParameterValue': os.environ[key]
        }
        for key, value in parameters.items()
    ]
)

print(response)
