import os
import sys
import logging
import argparse

from src.DataSource import DataSource
from config import *

logging.basicConfig()
logger = logging.getLogger('main')
logger.setLevel(LOG_LEVEL)

parser = argparse.ArgumentParser(
    prog='DataSource',
    description='A command line tool to generate lambda events from csv files.'
)

parser.add_argument('filename')
parser.add_argument('directoryPath')



def main(data_source: DataSource):

    data_source.readLineEventLoop(5)


if __name__ == '__main__':
    args = parser.parse_args()
    logger.debug(f'arg object: {args}')
    logger.debug(args.filename)

    main(DataSource(args.filename, args.directoryPath))
