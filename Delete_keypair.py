import boto3
client = boto3.resource('ec2')
response = client.delete_key_pair(
    KeyName='testing123',
    KeyPairId='key-00080e19217d07715',
    DryRun=True|False
)