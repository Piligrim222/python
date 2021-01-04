import tkinter


class TrafficLight():
    def __init__(self):
        self.__color = "grey"
        self.myDict = {"red": [7, 1], "yellow": [2, 2], "green": [timeGreen, 3]}
        self.colors = (i for i in self.myDict)
        print(self.colors)
        self.canvas = tkinter.Canvas(wnd, width=dimensions[0], height=dimensions[1], bg="black")
        for i in range(3):
            self.canvas.create_oval(20, 20 + (dimensions[2] + 20) * i, w - 20,
                                    20 + dimensions[2] + (dimensions[2] + 20) * i, fill=self.__color)
        self.canvas.pack()
        wnd.update()

    def greyLight(self):
        self.canvas.itemconfig(self.myDict[self.color][1], fill="grey")
        self.running()

    def running(self):
        try:
            self.color = next(self.colors)
        except StopIteration:
            self.colors = (i for i in self.myDict)
            self.color = next(self.colors)
        self.canvas.itemconfig(self.myDict[self.color][1], fill=self.color)
        wnd.after(self.myDict[self.color][0] * 1000, self.greyLight)




# timeGreen = int(input("Введите время работы зеленого цвета: "))
timeGreen = 5
wnd = tkinter.Tk()
w = 180
dimensions = [w, (w - 40) * 3 + 80, w - 40]
wnd.minsize(dimensions[0], dimensions[1])
wnd.maxsize(dimensions[0], dimensions[1])
wnd.title("Светофор")
a = TrafficLight()
try:
    print(a.__color)
except AttributeError:
    print("реализован приватный тип атрибута __color")
a.running()
wnd.mainloop()

