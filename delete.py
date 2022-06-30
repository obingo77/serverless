import boto3

sfn_client = boto3.client('stepfunctions')

state_machine_arn = 'arn:aws:states:ap-northeast-1:585584209241:stateMachine:ProcessTransactionStateMachine'

response = sfn_client.delete_state_machine(
    stateMachineArn=state_machine_arn
)

print(response)