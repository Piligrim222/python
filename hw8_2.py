class ZeroDivError(Exception):
    def __init__(self, text):
        pass


inputOne = input("Введите первое число: ")
inputTwo = input("Введите второе число: ")

try:
    inputOne = int(inputOne)
    inputTwo = int(inputTwo)
    if inputTwo == 0:
        raise ZeroDivError("Делите на ноль осторожней :'(")
except ValueError:
    print("Это не число(а)")
except ZeroDivError as myError:
    print(myError)
else:
    print(inputOne / inputTwo)
