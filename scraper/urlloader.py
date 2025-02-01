class URLLoader:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        with open(self.file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
