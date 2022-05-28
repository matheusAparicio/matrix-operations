def isNumber(str: str):
    try:
        float(str)
        return True
    except:
        return False