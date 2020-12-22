print("Здравствуйте! В данной задаче необходимо ввести элементы списка через пробелы, или запятые."
      "Либо ввести целую строку. В первом случае поменяются элементы, во втором символы строки")
my_list = input("Вводить здесь --> ")

# my_list = "1 2 3 4 5 6 7 8 9"
# my_list = "1,2,3,4,5,6,7,8,9"
# my_list = "12345678"

string = ""
if my_list.find(" ") == -1 and my_list.find(",") == -1:
    for i in range(0, len(my_list), 2):
        string += ''.join(reversed(my_list[i:i + 2]))
    print(string)
else:
    my_list = my_list.split()
    if len(my_list) == 1:
        my_list = my_list[0].split(",")
    test = len(my_list)
    if len(my_list) % 2 != 0:
        my_list.append(my_list[-1])
    for i in range(0, len(my_list), 2):
        buf = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = buf

    print(my_list if test % 2 == 0 else my_list[0:-1])
