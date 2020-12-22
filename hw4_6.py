from itertools import count, cycle

my_list = []

for i in count(3):
    my_list.append(i)
    if i == 10:
        break

print(my_list)

j = 0
for i in cycle(my_list):
    print(i)
    j += 1
    if j == 30:
        break
