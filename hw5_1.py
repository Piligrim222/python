with open("testFile.txt", "w", encoding="utf-8") as file:
    while (line := input("Программа выполняется, ничего не делайте тут -> ")) != "":
        file.writelines(line + "\n")
