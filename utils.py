class Key():
    def __init__(self, path):
        with open(path, 'r') as file:
            self.key = file.read()    
    