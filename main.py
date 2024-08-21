import os
import sys
import time
import logging
import boto3

from DataSource import DataSource

DEST_ARN = os.getenv('DEST_LAMBDA_ARN')

logging.basicConfig()
logger = logging.getLogger('main')
logger.setLevel('DEBUG')

# lambda_client = boto3.client('lambda')


def main(data_source: DataSource):

    with open(f'data/{data_source.file_name}', 'r') as fe:
        cols_energy = fe.readline()
        # logger.debug(cols)
        for line in fe:
            next_line = fe.readline()
            # logger.debug(next_line)
            time.sleep(5)

            event = {'cols': cols_energy, 'record': next_line}
            print(event)

            # response = lambda_client.invoke(
            #     FunctionName=DEST_ARN,
            #     InvocationType='Event',
            #     Payload=event
            # )




if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        print(file_name)
    except Exception as e:
        raise Exception('No file name provided')

    main(DataSource(file_name))
