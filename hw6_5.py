class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    def draw(self):
        return "Уникальное сообщение для класса Pen. " + super().draw()


class Pencil(Stationery):
    def draw(self):
        return "Уникальное сообщение для класса Pencil. " + super().draw()


class Handle(Stationery):
    def draw(self):
        return "Уникальное сообщение для класса Handle. " + super().draw()


a = Pen("рисунок нумбер one")
b = Pencil("рисунок нумбер two")
c = Handle("рисунок нумбер three")
print(f"'{a.draw()}' в начале рисования рисунка '{a.title}'.")
print(f"'{b.draw()}' в начале рисования рисунка '{b.title}'.")
print(f"'{c.draw()}' в начале рисования рисунка '{c.title}'.")
