import boto3
x = boto3.resource('ec2')
response = x.delete_key_pair(KeyName='testing123',KeyPairId='key-00080e19217d07715')