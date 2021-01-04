from time import sleep
import turtle


class TrafficLight:
    def __init__(self):
        self.__color = "grey"
        w = 240
        h = (w - 40) * 3 + 80
        self.coordinates = {"red": (w - 40) / 2 + 20,"yellow": 0 - (w - 40) / 2, "green": 0 - h / 2 + 20}
        self.radius = (w - 40) / 2
        self.t = turtle.Turtle()
        self.start(w, h)

    def running(self, timeGreen=5):
        myDict = {"red": 7, "yellow": 2, "green": timeGreen}
        for color in myDict:
            self.timerLight(self.coordinates[color], color, myDict[color])
            self.timerLight(self.coordinates[color], self.__color, 0)
        self.t.screen.exitonclick()

    def timerLight(self, coord, color, time):
        t = self.t
        t.up()
        t.goto(0, coord)
        t.down()
        t.begin_fill()
        t.fillcolor(color)
        t.circle(self.radius, 360)
        t.end_fill()
        if time > 0:
            for tm in range(time, 0, -1):
                sleep(0.5)
                t.write(tm, False, "center", font=("Arial", 36, 'normal'))
                sleep(0.5)
                t.begin_fill()
                t.circle(self.radius, 360)
                t.end_fill()

    def start(self, w, h):
        t = self.t
        t.screen.title("Светофор")
        t.screen.setup(w + 70, h + 70)
        t.shape("turtle")
        t.penup()
        t.goto(0 - w / 2, h / 2)
        t.pendown()
        t.begin_fill()
        t.fillcolor("black")
        for _ in range(2):
            t.fd(w)
            t.right(90)
            t.fd(h)
            t.right(90)
        t.end_fill()
        t.hideturtle()
        t.speed(1024)
        self.timerLight(self.coordinates["red"], self.__color, 0)
        self.timerLight(self.coordinates["yellow"], self.__color, 0)
        self.timerLight(self.coordinates["green"], self.__color, 0)


#timeGreen = int(input("Введите время работы зеленого цвета: "))
a = TrafficLight()
try:
    print(a.__color)
except AttributeError:
    print("реализован приватный тип атрибута __color")
a.running()
