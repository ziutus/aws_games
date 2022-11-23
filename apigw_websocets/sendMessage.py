import json
import boto3

session = boto3.Session(
    aws_access_key_id="",
    aws_secret_access_key="",
    aws_session_token=""
)

params = {
    'region': 'eu-west-1',
    'connectionId': 'cAdRPe6wjoECEpQ='
}

client = session.client('apigatewaymanagementapi', region_name=params["region"],
                        endpoint_url='https://agkkq9sn04.execute-api.eu-west-1.amazonaws.com/Prod')

for number in range(10):
    response = client.post_to_connection(
        Data=json.dumps({'test': number}),
        ConnectionId= params['connectionId']
    )
