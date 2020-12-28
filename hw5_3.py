file = [i.rstrip() for i in open("text_3.txt", "r", encoding="utf-8")]
print(file)
sum = 0
for line in file:
    line = line.rstrip().split()
    sum += float(line[1])
    if float(line[1]) < 20000.0:
        print(line[0], line[1])
print(f"\nСредняя: {sum / len(file):.2f}")
