import boto3
ec2 = boto3.resource('ec2')
"""vpc = ec2.create_vpc(
    CidrBlock='10.0.0.0/16',InstanceTenancy='default')"""
security_group = ec2.create_security_group(
    Description='Sample',
    GroupName='MySecGroup',
    VpcId='vpc-0b1aa6dee080ac158',
    TagSpecifications=[
        {
            'ResourceType': 'security-group',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'MySecgroup'
                },
            ]
        },
    ],
)   
subnet = ec2.create_subnet(AvailabilityZone='ap-southeast-1b',
    CidrBlock='10.0.0.0/24',
    VpcId='vpc-0b1aa6dee080ac158',
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'MySubnet'
                },
            ]
        },
    ],
)    
