file = [i.rstrip() for i in open("testTest.txt", "r", encoding="utf-8")]
print(f"Всего строк {len(file)}.")
words = ["слово", "слова", "слов"]
for i in range(len(file)):
    print(f"В строке {i + 1} - {(indx := len(file[i].split()))} {words[2 if (0 < indx % 10 < 5 and indx // 10 % 10 == 1) or indx % 10 == 0 or 4 < indx % 10 < 11 else 0 if indx % 10 == 1 else 1]}.")
