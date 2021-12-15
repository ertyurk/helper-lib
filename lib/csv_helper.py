import csv  
import os.path
from os import path
class CsvCreator:
    def __init__(self, filename, permission):
        if path.isdir('media') == False:
            os.mkdir('media')
        self.filename = filename
        self.permission = permission
        self.writer = csv.writer(open(f"media/{filename}", self.permission, encoding='UTF8'))

    def add_header(self, data):
        self.writer.writerow(data)

    def add_row(self, data):
        self.writer.writerow(data)

    def read(self):
        return list(csv.reader(open(f"media/{self.filename}", self.permission, encoding='UTF8')))
