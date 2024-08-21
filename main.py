import os
import sys
import logging

from src.DataSource import DataSource
from src.config import *

os.environ['DEST_LAMBDA_ARN'] = DEST_LAMBDA_ARN

logging.basicConfig()
logger = logging.getLogger('main')
logger.setLevel(LOG_LEVEL)



def main(data_source: DataSource):

    data_source.readLineEventLoop(5)


if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        print(file_name)
    except Exception as e:
        raise Exception('No file name provided')

    main(DataSource(file_name))
