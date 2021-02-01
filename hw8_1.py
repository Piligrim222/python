class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def toDigit(cls, date):
        date = list(map(int, date.split("-")))
        return date

    @staticmethod
    def valid(date):
        flag = 0
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if date[2] > 0:
            flag += 1
        if flag == 1 and date[1] in range(1, 13):
            flag += 1
        if flag == 2:
            if date[2] % 4 == 0:
                if date[2] % 400 == 0:
                    months[2] = 29
                if date[2] % 100 == 0:
                    pass
                else:
                    months[2] = 29
            if date[0] in range(1, months[date[1]] + 1):
                flag += 1
        return True if flag == 3 else False

a = Date("29-02-2100")
print(Date.valid(Date.toDigit("28-02-2100")))