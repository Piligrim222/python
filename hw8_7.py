from re import findall


class Compl:
    def __init__(self, num):
        if not num.isdigit():
            test = findall(r'(-*\d*){0,1}?\+*(-*\d*)i', num)[0]
            if test[0] == "":
                x = 0
            else:
                x = int(test[0])
            if test[1] == "":
                y = 1
            elif test[1] == "-":
                y = -1
            else:
                y = int(test[1])
        else:
            x = int(num)
            y = 0
        self.ttt = [x, y]

    def answer(self, t, r):
        if t == 0:
            text_1 = ""
        else:
            text_1 = str(t)
        if r == 0:
            text_2 = ""
        elif r == 1:
            text_2 = "i"
        elif r == -1:
            text_2 = "-i"
        else:
            text_2 = str(r) + "i" if r < 0 else "+" + str(r) + "i"
        return text_1 + text_2

    def __add__(self, other):
        t = self.ttt[0] + other.ttt[0]
        r = self.ttt[1] + other.ttt[1]
        return self.answer(t, r)

    def __mul__(self, other):
        t = self.ttt[0] * other.ttt[0] - self.ttt[1] * other.ttt[1]
        r = self.ttt[0] * other.ttt[1] + other.ttt[0] * self.ttt[1]
        return self.answer(t, r)


a = Compl("3+i")
b = Compl("2-3i")
c = Compl("-4i")
d = Compl("4")
e = Compl("3-i")
print(a * b)
print(a * c)
print(a * d)
print(a + b)
print(a + c)
print(a + e)
