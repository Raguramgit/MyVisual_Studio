import boto3
ec2 = boto3.resource('ec2')
ec2.create_volume(AvailabilityZone='ap-southeast-1a',Size=10,VolumeType='gp3')