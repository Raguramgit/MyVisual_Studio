import boto3
client = boto3.client('ec2')
client.attach_volume(
    Device='xvdf',
    InstanceId='i-058ddb14526f180c9',
    VolumeId='vol-01c0b288f9a3bac66')