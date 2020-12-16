my_list = [7, 5, 3, 3, 2]
inp = int(input("Введите любое число не дробное, можно даже отрицательное: "))
i = 0

while i in range(len(my_list)):
    if inp > my_list[i]:
        my_list.insert(i, inp)
        j = i
        break
    elif i == len(my_list) - 1:
        my_list.append(inp)
        j = i + 1
        break
    i += 1

print(f"Вы ввели число {inp}. Оно вставлено на позицию {j}. Результат: {str(my_list)[1:-1]}")

my_list = [7, 5, 3, 3, 2]
if i == 0:
    new_list = [inp] + my_list
elif inp > my_list[i]:
    new_list = my_list[:i] + [inp] + my_list[i:]
elif i == len(my_list) - 1:
    print(i)
    new_list = my_list + [inp]
    i += 1

print(f"Вы ввели число {inp}. Оно вставлено на позицию {i}. Результат: {str(new_list)[1:-1]}")
