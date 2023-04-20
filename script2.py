import boto3
import yaml
import os

myclient2 = boto3.client('ec2','us-east-2')
iam = boto3.client('iam')

role_name = 'accessS3UsingEc2'
policy_name = "accessS3"


with open('ec2.yml','r') as e:
    mydata2 = yaml.safe_load(e)
    if(os.environ['InstanceType']):
        mydata2["InstanceType"] = os.environ['InstanceType']
    if(os.environ['InstanceName']):
        print(mydata2["TagSpecifications"])
        mydata2["TagSpecifications"][0]["Tags"][0]["Value"] = os.environ['InstanceName']

with open("ec2.yml", "w") as f:
    yaml.dump(mydata2, f)

with open('ec2.yml','r') as e:
    mydata2 = yaml.load(e,Loader=yaml.FullLoader)

response = iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument='''{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }'''
)
bucket_name = os.environ['BucketName']
policy = {
    'Version': '2012-10-17',
    'Statement': [
        {
            'Effect': 'Allow',
            'Action': [
                's3:GetObject',
                's3:PutObject',
                's3:PutObjectAcl'
            ],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }
    ]
}

iam.put_role_policy(RoleName=role_name,PolicyName=policy_name,PolicyDocument=json.dumps(policy))
iam.create_instance_profile(InstanceProfileName=role_name)


myclient2.run_instances(**mydata2+f",IamInstanceProfile={{'Name': {role_name}}}")
