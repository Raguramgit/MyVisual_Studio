from http import client
import boto3
x = boto3.resource('ec2')
response = client.delete_key_pair(
    KeyName='string',
    KeyPairId='string',
    DryRun=True|False
)