def my_func(num1, num2, num3):
    return num1 + num2 + num3 - min(num1, num2, num3)


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
print(my_func(num1, num2, num3))
