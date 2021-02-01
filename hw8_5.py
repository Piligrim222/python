class Sklad:
    def __init__(self, myDict):
        self.myDict = myDict
        print(f"Создан склад {self.myDict}")

    def priem(self, tip, kolichestvo):
        self.myDict[tip] += kolichestvo
        print(f"На склад добавлено {kolichestvo} {tip}. Итог: {self.myDict}")

    def uhod(self, otdel, tip, kolichestvo):
        if self.myDict[tip]-kolichestvo < 0:
            print(f"Такого количества нет, забирайте {self.myDict[tip]} {tip}.")
            self.myDict[tip] = 0
            print(f"На складе осталось: {self.myDict}")
        else:
            self.myDict[tip] -= kolichestvo
            print(f"Забрано {kolichestvo} {tip} в отдел '{otdel}'.\nНа складе осталось: {self.myDict}")


class Orgtehnika:
    def __init__(self, kolichestvo):
        self.kolichestvo = kolichestvo

    def sozdanie(self):
        return self.kolichestvo


class Printer(Orgtehnika):
    pass


class Skaner(Orgtehnika):
    pass


class Kseroks(Orgtehnika):
    pass


prs = Printer(2)
sks = Skaner(5)
kss = Kseroks(10)

skl_1 = Sklad({"Printer": prs.sozdanie(), "Skaner": sks.sozdanie(), "Kseroks": kss.sozdanie()})
skl_1.priem("Printer", 0)
skl_1.priem("Skaner", 0)
skl_1.priem("Kseroks", 1)

skl_1.uhod("otdel_1", "Printer", 6)
skl_1.uhod("otdel_2", "Skaner", 1)
