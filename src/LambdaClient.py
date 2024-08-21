import boto3
import logging
import json

from src.config import *

logging.basicConfig()
logger = logging.getLogger('LambdaClient')
logger.setLevel(LOG_LEVEL)


class LambdaClient:
    lambda_client = None
    def __init__(self):
        if self.lambda_client == None:
            self.lambda_client = boto3.client('lambda')


    def invokeAsync(self, destination_arn: str, event: dict):
        logger.debug(f'Sending event to {destination_arn}')
        response = self.lambda_client.invoke(
            FunctionName=destination_arn,
            InvocationType='Event',
            Payload=json.dumps(event).encode()
        )
