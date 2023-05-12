import boto3
x = boto3.resource('ec2')
x.create_key_pair(KeyName='EBS')