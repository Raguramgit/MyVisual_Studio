import boto3
client = boto3.client('ec2')
"""client.attach_volume("""
client.detach_volume(
    Device='xvdh',
    InstanceId='i-077eedcdaa8e433fd',
    VolumeId='vol-098688dd285f73dc8')