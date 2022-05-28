
from utilities.isNumber import isNumber


class Scan:

    def __init__(self, path: str):
        self.file = open(path, "r").readlines()
        self.matrix1 = []
        self.matrix2 = []
        self.matrixResult = []
        self.currentLine = 0
        self.maxSearchLines = 10

    def findMatrix(self):
        for i, lineContent in enumerate(self.file):
            if isNumber(lineContent[0]):
                self.currentLine = i
                return 0
            self.currentLine += 1

    def saveMatrix(self):
        print(self.currentLine)