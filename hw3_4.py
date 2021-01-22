def my_func2(x, y):
    res = 1
    for _ in range(0 - y):
        res *= x
    return 1 / res


my_func = lambda x, y: 1 / (x ** (0 - y))

x = int(input("Введите действительное положительное число: "))
y = int(input("введите целое отрицательное число: "))
print(my_func2(x, y))
print(my_func(x, y))
