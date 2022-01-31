"""

    *** Event pattern in Cloud Watch / EventBridge targetting a Lambda function

    {
        "source": ["aws.s3"],
        "detail-type": ["AWS API Call via CloudTrail"],
        "detail": {
            "eventSource": ["s3.amazonaws.com"],
            "eventName": ["CreateBucket"]
         }
    }
"""

import boto3
import json
import sys


def enable_s3_encryption_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    client = boto3.client('s3')
    try:
        bucket_name = event['detail']['requestParameters']['bucketName']
        client.put_bucket_encryption(Bucket=bucket_name,
                        ServerSideEncryptionConfiguration={
                        'Rules': [
                            {
                                'ApplyServerSideEncryptionByDefault': {
                                    'SSEAlgorithm': 'AES256'
                                }
                            },
                        ]
                        })
        print(f'SSE Encryption has been ENABLED for bucket: {bucket_name}')
    except Exception as e:
        print(e)
        sys.exit(1)