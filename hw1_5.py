profit = int(input("Введите прибыль Фирмы в местной валюте: "))
costs = int(input("Введите издержки Фирмы в местной валюте: "))
result = profit - costs
if result > 0:
    print("Фирма отработала с прибылью")
    print(f"Рентабельность составила {result / profit:.2f}")
    print()
    employees = int(input("Введите количество сотрудников в Фирме: "))
    print()
    print(f"Прибыль Фирмы в расчете на каждого сотрудника составила {result / employees:.2f} БЧС")
    print("БЧС - большое человеческое спасибо")
elif result < 0:
    print("Фирма отработала в убыток")
else:
    print("Фирма отработала без прибыли и убытка")
