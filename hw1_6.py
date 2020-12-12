start = int(input("Результат в первый день, километров: "))
finish = int(input("Необходимо достигнуть, километров: "))
day = 1
while True:
    if start > finish:
        break
    start *= 1.1
    day += 1
print(f"на {day}-й день спортсмен достиг результата — не менее {finish} км.")
