import json
import boto3

session = boto3.Session(
    aws_access_key_id="ASIA4MCSWRSGYFYR7HOU",
    aws_secret_access_key="UtAjYNgSvzD/2FeDKWPNtclYBFQPj/Qd6X4keT9P",
    aws_session_token="IQoJb3JpZ2luX2VjEJ3//////////wEaCWV1LXdlc3QtMSJIMEYCIQC0bgPlBYS7WSvWy7hsY1TJC4nnL1QnHR16KHEGwP+j8QIhAM9AUSWC75RnSB2/zmRIXXpRUN38bs6AYEGye8s2XUiEKv8CCKb//////////wEQAhoMODUwNTc2OTY4ODQ1IgxuDyYtyhwMYbjr4d4q0wIsNgONwpFnBs0kiJAoIQXGZ1smSMaui0Ey/f0cBW+Qh3pjTbYZOSiJQlC7O1YhKuRWmqVhKahczhtcCKnd9GA5MH/hUG0EjLYcRsGR0hke6YdbVjbAK8tH+SslESSxPgTA1TdpWuZuBNO4jwXljm4hep3Ct4AyjrMKJo4oRR2o7gyOmwX8Ej0WKtcXN608jlQfAnCDI5KKS8G+0rc2zFW/z/0ONzBJIiYjcWNu/nGp8hExgMyuxunTSJWRg73iDKu6kZc9YYq3lx18PU91xRfR474/Ebc/kAvWwpCPD3CCYhj4OsdZIk5OnzzfK+YU6o/jV/0xojFnzwaX69SwYPwzhFPc8p5GJsvPBI1G1KKheXrm5XmT9TnmsO2O8D4IDjyPqFktvrBR57KiIUONimTJwjlvcBnRHWIN4cu5j1ekU25p1IfPsIlPoR8dFUvvlMdkdIAwjf/ymwY6pQFWl1DNowjoCrC3TTU23kMDO5jA2ftZtyNZWPkP+6mCNel7w5DxvuQguPgHneSxubcpDmF8yc66Zs2cq6gGvx8D8zFVsRrNFMLTCgFRw76OiI4LVmdbJ/S+TG67vY3v3FTo4WiUHpIxeP6fco5MTpf8Ol4XcLu1jQg5yLLNAVrBNEQgvQC7YGvp5yozOqa0Hltba4bcklKkP0eQxdFJKHe/gW8zcSQ="
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
