int_func = lambda a: a[0].upper() + a[1:]

fullLine = input().split()
for line in fullLine:
    flag = 1
    for i in line:
        if i not in "qwertyuiopasdfghjklzxcvbnm":
            flag = 0
    if flag == 1:
        print(int_func(line), end=' ')
    else:
        print(line, end=' ')
