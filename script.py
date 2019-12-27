#! /usr/local/bin/python3
import logging
import boto3
import time
import sys

from botocore.exceptions import ClientError

if len(sys.argv) < 2:
    print("A bucket name must be passed in via command line: `./script.py <bucket-name> <region>`")
    exit(1)

bucket_name = sys.argv[1]
try:
    region=sys.argv[2]
except:
    region=None
old_error = ""
try_counter = 0

print('Start Time: '+time.strftime('%a %H:%M:%S'))

def create_bucket(bucket_name, region):
    # Create bucket
    global old_error
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        e = str(e)
        if e == old_error:
            old_error = e
            return False
        else:
            logging.error(e)
            old_error = e
            return False
    return True

while 1==1:
    timestamp = time.strftime('%a %H:%M:%S')
    print('Attempt: ' + str(try_counter) + " | "+ timestamp, end="\r", flush=True)
    bucket_status = create_bucket(bucket_name, region)
    if bucket_status == True:
        print("Bucket Created: " + timestamp)
        exit()
    else:
        try_counter = try_counter+1
        time.sleep(2)
        continue
