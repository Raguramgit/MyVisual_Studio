from re import X
import boto3
x = boto3.resource('ec2')
x.create_volume(AvailabilityZone='ap-southeast-1a',Size=10,VolumeType='gp3')