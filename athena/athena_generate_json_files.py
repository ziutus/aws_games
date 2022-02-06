import json
from random import random, randrange, sample
from datetime import datetime, timedelta
import boto3


number_of_files = 30
number_of_records = randrange(1, 30, 1)

headers = [
     "temperature", "pressure", "humidity", "brightness", "saturation"
]

record_id = 1
for fileNumber in range(1, number_of_files, 1):
    content = ""
    filename = None
    print(f"Number of records: {number_of_records}")
    for i in range(0, number_of_records):
        random_minutes = randrange(0, 59, 1)
        timestamp = datetime.now() - timedelta(minutes=random_minutes)
        # print(timestamp.strftime('%Y-%m-%d_%H:%M:%S'))
        filename = f"sensors_raw/{timestamp.strftime('%Y%m%d_%H%M%S')}_{fileNumber}.json"

        data_set = {}
        # data_set["record_id"] = record_id
        record_id += 1
        data_set["sensor_id"] = randrange(1, 20, 1)
        data_set["timestamp"] = timestamp.timestamp()

        current_headers = sample(headers, randrange(2, len(headers), 1))

        for header in current_headers:
            data_set[header] = randrange(0, 100, 1)

        json_dump = json.dumps(data_set)
        print(json_dump)
        # json_object = json.loads(json_dump)
        # print(json_object["key1"])
        content += json_dump + "\n"

    s3 = boto3.resource(
        's3',
        region_name='eu-central-1',
        aws_access_key_id="XXX",
        aws_secret_access_key="YYY"
    )

    s3.Object('odkrywca-qa-athena-games', filename).put(Body=content)