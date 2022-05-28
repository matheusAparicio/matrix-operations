from scan import Scan

scan = Scan("example.txt")

if __name__ == '__main__':
    scan.saveMatrices()
    #scan.multiplyMatrices()
    print(f"Matriz 0: {scan.matrix0}\n")
    print(f"Matriz 1: {scan.matrix1}\n")
    #print(f"Matriz Resultado: {scan.matrixRealResult}\n")