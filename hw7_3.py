class Cell:
    def __init__(self, sum):
        self.sum = sum

    def __add__(self, other):
        return self.sum + other.sum

    def __sub__(self, other):
        if ((a := self.sum - other.sum) > 0):
            return a
        else:
            print("Вычитание выполнить нельзя!")
            return 0

    def __mul__(self, other):
        return self.sum * other.sum

    def __floordiv__(self, other):
        try:
            return self.sum // other.sum
        except ZeroDivisionError:
            print("Деление выполнить нельзя!")
            return 0

    def make_order(self, sumRow):
        myList = ["*" * sumRow for _ in range(self.sum // sumRow)]
        if (b := self.sum % sumRow) > 0:
            myList.append("*" * b)
        return "\n".join(myList) if len(myList) != 0 else "Клетки нема ¯\_(ツ)_/¯"

    def make_order_2(self, sumRow):
        myAnswer = "*" * (c := self.sum % sumRow)
        for _ in range(self.sum // sumRow):
            myAnswer = "*" * sumRow + "\n" + myAnswer
        if len(myAnswer) != 0:
            return myAnswer if c > 0 else myAnswer[:-1]
        else:
            return "Клетки нема ¯\_(ツ)_/¯"


a = Cell(13)
b = Cell(0)
print("Клетка a")
print(a.make_order(5))
print("Клетка b")
print(b.make_order_2(5))
print("Сложение клеток a и b")
print(Cell(a + b).make_order(5))
print("Вычитание клеток a из b")
print(Cell(a - b).make_order_2(5))
print("Вычитание клеток b из a")
print(Cell(b - a).make_order(5))
print("Умножение клеток a и b")
print(Cell(a * b).make_order(75))
print("Деление клеток a на b")
print(Cell(a // b).make_order(75))
print("Деление клеток b на a")
print(Cell(b // a).make_order(75))
