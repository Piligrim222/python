from sys import argv

try:
    argv = list(map(int, argv[1:]))
    if len(argv) % 3 != 0 or len(argv) == 0:
        print("Ooops")
    else:
        print([(argv[i] * argv[i + 1] + argv[i + 2]) for i in range(0, len(argv), 3)])
except:
    print("Ooops")

