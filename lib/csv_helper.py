import csv  

class CsvCreator:
    def __init__(self, filename, permission):
        self.filename = filename
        self.permission = permission
        self.writer = csv.writer(open(f"media/{filename}", self.permission, encoding='UTF8'))

    def add_header(self, data):
        self.writer.writerow(data)

    def add_row(self, data):
        self.writer.writerow(data)

    def read(self):
        return list(csv.reader(open(f"media/{self.filename}", self.permission, encoding='UTF8')))
