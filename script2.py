import boto3
import yaml

myclient2 = boto3.client('ec2','us-east-2')

with open('ec2.yml','r') as e:
    mydata2 = yaml.load(e,Loader=yaml.FullLoader)

myclient2.run_instances(**mydata2)