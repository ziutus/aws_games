# AWS Websocket API Gateway 

## A example AWS application
There is example application prepared by AWS team [simple-websockets-chat-app](https://github.com/aws-samples/simple-websockets-chat-app)
It contains API Gateway, Lambdas and DynamoDB table to keep information about connections.
it exist on [Applications](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:729047367331:applications~simple-websockets-chat-app)



## Testing applications

You can test this application by using [wscat](https://github.com/websockets/wscat) tool. It exist in pip:

```shell
sudo npm install -g wscat
```

And you can test your API Gateway calling below command (-c is to connect)

```shell
wscat -c wss://agkkq9sn04.execute-api.eu-west-1.amazonaws.com/Prod
```
And now you can send some data. The "action part" will route it to target Serverless function:

```shell
{ "action": "sendmessage", "data": "Test message" }
```


If you want to use curl, you will be see error about missing headers:
```shell
curl -X POST -d "hello world" https://agkkq9sn04.execute-api.us-east-1.amazonaws.com/Prod/@connections/{connection_id}
curl -X POST -d "hello world" https://agkkq9sn04.execute-api.us-east-1.amazonaws.com/Prod/@connections/b9Y4idZZDoECH3A=
```

To avoid this, you can use [awscurl](https://github.com/okigan/awscurl):

```shell
awscurl --profile odkrywca-dev1 --region eu-west-1  --service execute-api  -X POST -d "hello test" https://agkkq9sn04.execute-api.eu-west-1.amazonaws.com/Prod/@connections/cAApXeTHDoECEKg=
```

## SDK, how to use it in application

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html

```python
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

```
[SDK link](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html)


## Interesting examples of usage
* [Graphql and subscriptions](https://www.yonomi.com/blog/graphql-subscriptions-over-aws-api-gateway-web-sockets)
* [Chat application](https://medium.com/artificial-industry/adding-websockets-to-your-aws-serverless-application-d8b1631754f6)


## Pricing and limits
[Pricing](https://aws.amazon.com/api-gateway/pricing/),
[Limits](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html#apigateway-execution-service-websocket-limits-table)

## Security
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html

## For future demos
* [Python WebSocket client](https://github.com/websocket-client/websocket-client)
* [PyCognito](https://pypi.org/project/pycognito/)
* [Python and websocket client for AppSync](https://aws.amazon.com/blogs/mobile/appsync-websockets-python/)
* [Python and webscket client for Api Gateway](https://www.youtube.com/watch?v=OJNjO7FrhOg)
* [Python and Cognito Part 1](https://medium.com/@houzier.saurav/aws-cognito-with-python-6a2867dd02c6), [Part 2](https://medium.com/@houzier.saurav/authentication-with-cognito-202977f8d64e), [Part3](https://medium.com/analytics-vidhya/private-api-endpoints-with-api-gateway-authorizers-and-cognito-249c288b0ab8) and [Part4](https://medium.com/analytics-vidhya/part-4-serverless-b0b7c8bdbd0a)