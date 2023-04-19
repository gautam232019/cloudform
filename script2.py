import boto3
import yaml
import os

myclient2 = boto3.client('ec2','us-east-2')

with open('ec2.yml','r') as e:
    mydata2 = yaml.safe_load(e)
    if(os.environ['InstanceType']):
        mydata2["InstanceType"] = os.environ['InstanceType']
    if(os.environ['InstanceName']):
        mydata2["TagSpecifications"][1][1] = os.environ['InstanceName']

with open("ec2.yml", "w") as f:
    yaml.dump(mydata2, f)

with open('ec2.yml','r') as e:
    mydata2 = yaml.load(e,Loader=yaml.FullLoader)

myclient2.run_instances(**mydata2)