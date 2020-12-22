from sys import argv

try:
    argv = list(map(int, argv[1:]))
    if len(argv) == 0:
        argv = input("Введите ряд чисел через пробел, либо введите '+', для использования статичного списка: ").split()
        if argv[0] == '+':
            argv = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
            print("Статичный список список: " + str(argv))
    argv = list(map(int, argv))
    print([argv[i] for i in range(1, len(argv)) if argv[i] > argv[i - 1]])
except:
    print("Ooops")
