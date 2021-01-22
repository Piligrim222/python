def funcResult(a1, a2):
    try:
        result = a1 / a2
        return f"Результат: {result}"
    except ZeroDivisionError:
        return "Вы ввели 0. Делить на ноль нельзя. Пока."

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(funcResult(num1, num2))
