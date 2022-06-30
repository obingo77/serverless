import boto3
import json

sfn_client = boto3.client('stepfunctions')

response = sfn_client.list_state_machines()

print(response)

