class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


a = Position("Alex", "Blake", "general manager", 50000, 100000)
b = Position("Elis", "Krump", "manager", 40000, 90000)
c = Position("Vasiliy", "Pupkin", "worker", 10000, 100)
print(f"{a.get_full_name()} на должности '{a.position}' получает {a.get_total_income()} тугриков")
print(f"{b.get_full_name()} на должности '{b.position}' получает {b.get_total_income()} тугриков")
print(f"{c.get_full_name()} на должности '{c.position}' получает {c.get_total_income()} тугриков")


