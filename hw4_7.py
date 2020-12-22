def fact(n):
    l = 1
    for i in range(1, n):
        l *= i
        yield f"{i}! = {l}"

try:
    n = int(input("Введите число, факториал которого Вас интересует: ")) + 1
    for el in fact(n):
        print(el)
except:
    print("Ooops")