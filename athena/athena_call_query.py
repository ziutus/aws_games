import boto3
import re
import time

params = {
    'region': 'eu-central-1',
    'database': 'default',
    'bucket': 'odkrywca-qa-athena-games',
    'path': 'temp/athena/output',
    'query': 'select * from sensors_data limit 10'
}

session = boto3.Session(
    aws_access_key_id="XXX",
    aws_secret_access_key="YYY"
)


def athena_query(client, params):
    response = client.start_query_execution(
        QueryString=params["query"],
        QueryExecutionContext={
            'Database': params['database']
        },
        ResultConfiguration={
            'OutputLocation': 's3://' + params['bucket'] + '/' + params['path']
        }
    )
    return response


def athena_to_s3(session, params, max_execution=5):
    client = session.client('athena', region_name=params["region"])
    execution = athena_query(client, params)
    execution_id = execution['QueryExecutionId']
    state = 'RUNNING'

    while (max_execution > 0 and state in ['RUNNING', 'QUEUED']):
        max_execution = max_execution - 1
        response = client.get_query_execution(QueryExecutionId=execution_id)

        if 'QueryExecution' in response and \
                'Status' in response['QueryExecution'] and \
                'State' in response['QueryExecution']['Status']:
            state = response['QueryExecution']['Status']['State']
            if state == 'FAILED':
                return False
            elif state == 'SUCCEEDED':
                s3_path = response['QueryExecution']['ResultConfiguration']['OutputLocation']
                filename = re.findall('.*\/(.*)', s3_path)[0]
                return filename
        time.sleep(1)

    return False


def cleanup(session, params):
    # Deletes all files in your path so use carefully!
    s3 = session.resource('s3')
    my_bucket = s3.Bucket(params['bucket'])
    for item in my_bucket.objects.filter(Prefix=params['path']):
        item.delete()

# Query Athena and get the s3 filename as a result
s3_filename = athena_to_s3(session, params)


params = {
    'region': 'eu-central-1',
    'database': 'default',
    'bucket': 'odkrywca-qa-athena-games',
    'path': 'temp/athena/output',
    'query': 'select * from sensors_data limit 10'
}

print(f" region: {params['region']}")
print(f" bucket: {params['bucket']}")
print(f" path: {params['path']}")
print(f"file with result is: {s3_filename}")

# Removes all files from the s3 folder you specified, so be careful
# cleanup(session, params)