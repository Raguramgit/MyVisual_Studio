import boto3
client = boto3.client('ec2')
client.delete_key_pair(KeyName='test',KeyPairId='key-0f39cabac1bdeb033')