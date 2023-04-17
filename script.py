import boto3
import yaml

# myclient = boto3.client('s3')

# with open('cf.yml','r') as f:
#     mydata = yaml.load(f,Loader=yaml.FullLoader)

# bucket_name = mydata['BucketName']
# # location = config.get('Location','us-east-2')
# myclient.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':'us-east-2'},)


myclient2 = boto3.client('ec2','us-east-2')

with open('ec2.yml','r') as e:
    mydata2 = yaml.load(e,Loader=yaml.FullLoader)

myclient2.run_instances(**mydata2)








