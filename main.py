from scan import Scan

scan = Scan("example.txt")

if __name__ == '__main__':
    scan.findMatrix()
    scan.saveMatrix()