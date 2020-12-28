import random

open("testText3.txt", "w").write(" ".join(map(str, [int(random.random() * 100) for _ in range(int(random.random() * 15))])))
print(f'Сумма: {sum(map(int, open("testText3.txt", "r").readline().split()))}')
