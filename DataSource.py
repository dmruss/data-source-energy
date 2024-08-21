import os


class DataSource:

    def __init__(self, file_name):
        files = os.listdir('./data')
        if not file_name.endswith('.csv'):
            file_name = file_name + '.csv'
        if file_name not in files:
            raise Exception('File does not exist')
        self.file_name = file_name

    def readLine