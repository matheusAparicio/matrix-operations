from utilities.isNumber import isNumber

def stringToFloat(str: str):
    numberList = []
    for i, number in enumerate(str):
        if number == "-":
                numberList.append(-float(str[i + 1]))
        elif isNumber(number) and str[i - 1] != '-':
            numberList.append(float(number))
    return numberList