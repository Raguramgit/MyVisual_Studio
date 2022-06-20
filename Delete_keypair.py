from http import client
import Delete_keypair
import boto3
import subprocess
x = boto3.resource('ec2')
x.delete_key_pair(KeyName='AWS',KeyPairId='key-03bfad0bbaeb3af79')