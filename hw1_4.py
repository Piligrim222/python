numb = int(input("Введите число: "))
i = 10
max = numb % i
while numb % i < numb:
    if (numb % i) // (i / 10) > max:
        max = (numb % i) // (i // 10)
        if max == 9:
            break
    i *= 10
print(max)
