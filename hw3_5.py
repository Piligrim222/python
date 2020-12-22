summa = 0
flag = True
while flag:
    inp = input("введите ряд чисел или фиг знает чего через пробелы: ")
    subSumma = 0
    for i in inp.split():
        if i.isdigit():
            summa += int(i)
            subSumma += int(i)
        elif "q" in i:
            flag = False
            break
        else:
            print("Вы ввели '" + i + "'. Для выхода введите 'q' (именно маленькую, нафиг обработку любых! Дисциплина превыше всего! "
                  "Держите себя в руках!) Можно слитно с любой фигнёй.")
    print(str(summa) + "(" + str(subSumma) + ")")
