import os
import time
import logging

from config import *
from src.LambdaClient import LambdaClient

logging.basicConfig()
logger = logging.getLogger('DataSource')
logger.setLevel(LOG_LEVEL)

class DataSource:

    def __init__(self, file_name, path):
        files = os.listdir(path)
        if not file_name.endswith('.csv'):
            file_name = file_name + '.csv'
        if file_name not in files:
            raise Exception('File does not exist')
        self.file_name = file_name

    def readLineEventLoop(self, sleep_seconds: int = 5):
        with open(f'data/{self.file_name}', 'r') as fe:
            cols = fe.readline()
            logger.debug(cols)
            for line in fe:
                next_line = fe.readline()
                logger.debug(next_line)

                event = {'cols': cols, 'record': next_line}
                logger.debug(event)

                LambdaClient().invokeAsync(DEST_LAMBDA_ARN, event)

                time.sleep(sleep_seconds)
