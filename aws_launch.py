
import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
# MaxCount = defines the no of instances to launch
# ImageID = dont forget to add image id

instances = ec2.create_instances (ImageId='ami-0c802847a7dd848c0',MinCount=1,MaxCount=3,InstanceType='t2.micro',KeyName='AWSkey')
