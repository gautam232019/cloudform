import boto3
import yaml
import os

myclient2 = boto3.client('ec2','us-east-2')
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct 

with open('ec2.yml','r') as e:
    mydata2 = yaml.load(e,Loader=yaml.FullLoader)
    mydictionary = Convert(mydata2)
    if(os.environ['InstanceType']):
        mydictionary["InstanceType"] = os.environ['InstanceType']
    if(os.environ['InstanceName']):
        mydictionary["TagSpecifications"]["Tags"]["Value"] = os.environ['InstanceName']

list = [(k, v) for k, v in mydictionary.items()]

with open("ec2.yml", "w") as f:
    yaml.dump(list, f)

with open('ec2.yml','r') as e:
    mydata2 = yaml.load(e,Loader=yaml.FullLoader)

myclient2.run_instances(**mydata2)