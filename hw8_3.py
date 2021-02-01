class ValError(Exception):
    def __init__(self, text):
        pass


myList = []
while True:
    inp = input("Для завершения необходимо ввести 'q'.\nВведите элемент списка: ")
    if inp == "q":
        if len(myList) == 0:
            print("Список пуст")
            break
        print(f"получившийся список: {str(myList)[1:-1]}")
        # print(*myList)
        break
    try:
        if not inp.isdigit():
            raise ValError("Ай-ай-ай...")
    except ValError as myError:
        print(myError)
    else:
        myList.append(int(inp))
