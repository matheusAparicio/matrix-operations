
class SomeClass:
    def __init__(self, someNumber):
        self.someNumber = someNumber
        pass

    def printHi(self, name):
        print(f"Hi, {name}. The chosen number was {self.someNumber}.")


someClass = SomeClass(5)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    someClass.printHi("Matheus")
