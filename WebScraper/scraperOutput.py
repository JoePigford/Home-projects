import json_awk as json

class output:

    def __init__(self, filename):
        self.filename = str(filename + ".json")

    def getConnection(self):
        self.file = open(self.filename, "w")










