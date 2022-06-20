import boto3
#ec2 = boto3.resource('ec2')
#ec2.create_volume(AvailabilityZone='ap-southeast-1b',Size=10,VolumeType='gp3')
client = boto3.client('ec2')
client.delete_volume(
    VolumeId='vol-098688dd285f73dc8')