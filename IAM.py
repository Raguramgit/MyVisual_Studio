import boto3
iam = boto3.resource('iam')
user = iam.User('Ram')
"""user = user.create(
    Path='/',
    PermissionsBoundary='arn:aws:iam::aws:policy/AdministratorAccess',
)"""
response = user.delete()