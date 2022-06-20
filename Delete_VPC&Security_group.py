from http import client
import boto3
client = boto3.client('ec2')
"ec2 = client.delete_security_group(
    GroupId='sg-0ccb22e1f593ef7f3',
)
ec2 = client.delete_subnet(
    SubnetId='subnet-069064dfefa6ff75a',
)
ec2 = client.delete_vpc(
    VpcId='vpc-0b1aa6dee080ac158',
)
