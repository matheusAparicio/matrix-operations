from utilities.isNumber import isNumber
from utilities.stringToFloat import stringToFloat
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
            if isNumber(lineContent[0]) or lineContent[0] == '-':
                self.foundMatrix = True
                if lineContent[-1] == '\n':
                    lineContent = lineContent[:-1]
                if lineContent[-1] == ' ':
                    lineContent = lineContent[:-1]

                if self.currentMatrix == 0:
                    print("aa")
                    self.matrix0.append(stringToFloat(lineContent))
                elif self.currentMatrix == 1:
                    self.matrix1.append(stringToFloat(lineContent))
                else:
                    self.matrixFileResult.append(stringToFloat(lineContent))
            self.currentLine += 1
            if self.foundMatrix and (self.currentLine < len(self.file) and not isNumber(self.file[self.currentLine][0]) and self.file[self.currentLine][0] != '-'):
                self.foundMatrix = False
                self.currentMatrix += 1

    def multiplyMatrices(self):
        if len(self.matrix0[0]) == len(self.matrix1):
            for i, line in enumerate(self.matrix0):
                resultLine = []
                for a, number in enumerate(line):
                    resultLine.append(number + self.matrix1[a][i])
                self.matrixRealResult.append(resultLine)
                resultLine = []
        else:
            print("O número de colunas da primeira matriz e de linhas da segunda são diferentes.")

    def sumMatrices(self):
        pass