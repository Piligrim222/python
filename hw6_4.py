class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.flag = 0

    def go(self):
        if self.flag == 0:
            self.flag = 1
            return f"Машина {self.name} поехала."
        else:
            return f"Машина {self.name} и так едет, не стоит этого делать."

    def stop(self):
        if self.flag == 1:
            self.flag = 0
            return f"Машина {self.name} остановилась."
        else:
            return f"Машина {self.name} и так стоит."

    def turn(self, direction):
        if self.flag == 1:
            return f"Машина {self.name} повернула {direction}."
        else:
            return f"Машина {self.name} стоит, приложите физическую силу и поверните машину {direction}."

    def show_speed(self):
        return f"Текущая скорость машины {self.name} составляет {self.speed} км/ч."


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return "Скорость превышена, но ничего страшного, штраф и так платить, едем дальше."
        else:
            return f"Текущая скорость машины {self.name} составляет {self.speed} км/ч."


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return "Скорость превышена, но ничего страшного, штраф и так платить, едем дальше."
        else:
            return f"Текущая скорость машины {self.name} составляет {self.speed} км/ч."


class PoliceCar(Car):
    pass


a = TownCar(70, "red", "Imya_1")
b = SportCar(120, "blue", "Imya_2")
c = WorkCar(50, "white", "Imya_3")
d = PoliceCar(1333734556, "gold", "Imya_4", True)
e = WorkCar(40, "purple", "Imya_5")
# машина a
print(a.go())
print(a.go())
print(a.turn("влево"))
print(a.stop())
print()
# машина b
print(b.go())
print(b.turn("вправо"))
print(b.stop())
print(b.turn("вправо"))
print()
# машина c
print(c.go())
print(c.turn("вверх"))
print(c.stop())
print(f"Машина {c.name}", "" if c.is_police else "не", "является полицейской.")
print()
# машина d
print(d.go())
print(d.turn("в космос"))
print(d.show_speed())
print(f"Машина {d.name}", "" if d.is_police else f"не", "является полицейской")
print(d.stop())
print()
# машина e
print(e.stop())
print(e.go())
print(e.turn("влево"))
print(e.show_speed())
print(e.stop())
