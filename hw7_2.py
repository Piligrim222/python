from abc import ABC


class Clothes(ABC):
    pass

class Coat(Clothes):
    @property
    def sum(self, V=2):
        return f"Для изготовления пальто размера '{V}' необходим отрез ткани длиной {V / 6.5 + 0.5:.2f} м."


class Suit(Clothes):
    def sum(self, H):
        return f"Для изготовления костюма ростом '{H}' необходим отрез ткани длиной {2 * H + 0.3:.2f} м."


print("Расчет необходимого объема ткани.")
while True:
    choice = int(input("1 - Пальто; 2 - Костюм; 0 - Выход: "))
    if choice == 1:
        a = Coat()
        print(a.sum)
        print("Spasibo!")
        break
    elif choice == 2:
        b = Suit()
        height = float(input("Для расчета необходимого количества ткани введите рост: "))
        print(b.sum(height))
        print("Spasibo!")
        break
    elif choice == 0:
        print("Spasibo!")
        break