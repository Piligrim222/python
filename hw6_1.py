from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self, timeGreen):
        myDict = {"\033[31mred": 7, "\033[33myellow": 2, "\033[32mgreen": timeGreen}
        for self.__color in myDict:
            self.timerLight(myDict[self.__color])

    def timerLight(self, time):
        print(self.__color, "\033[0m")
        for i in range(time, 0, -1):
            sleep(0.5)
            print(i, end=" ")
            sleep(0.5)
        print()


timeGreen = int(input("Введите время работы зеленого цвета: "))
a = TrafficLight()
try:
    print(a.__color)
except AttributeError:
    print("реализован приватный тип атрибута __color")
a.running(timeGreen)
