
from utilities.isNumber import isNumber


class Scan:

    def __init__(self, path: str):
        self.file = open(path, "r").readlines()
        self.matrix0 = []
        self.matrix1 = []
        self.matrixRealResult = []
        self.matrixFileResult = []
        self.currentLine = 0
        self.currentMatrix = 0 # 0 = self.matrix0, 1 = self.matrix1, 2 = self.matrixResult
        self.foundMatrix = False

    def saveMatrices(self):
        while self.currentLine < len(self.file):
            lineContent = self.file[self.currentLine]
            if isNumber(lineContent[0]):
                self.foundMatrix = True
                if lineContent[-1] == '\n':
                    lineContent = lineContent[:-1]
                if lineContent[-1] == ' ':
                    lineContent = lineContent[:-1]
                if self.currentMatrix == 0:
                    self.matrix0.append(lineContent)
                elif self.currentMatrix == 1:
                    self.matrix1.append(lineContent)
                else:
                    self.matrixFileResult.append(lineContent)
            self.currentLine += 1
            if self.foundMatrix and self.currentLine < len(self.file) and not isNumber(self.file[self.currentLine][0]):
                self.foundMatrix = False
                self.currentMatrix += 1