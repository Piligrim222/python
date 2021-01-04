class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self):
        return self._length * self._width * 25 * 5


a = Road(5000, 20)
result = a.calculation()
print(f"{result} кг или {result // 1000} т")
