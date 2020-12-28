import json

myDict, myDict1, j, sum = {}, {"average_profit": 0}, 0, 0
with open("text_7.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.split()
        myDict[line[0]] = int(line[2]) - int(line[3])
for i in myDict:
    if myDict[i] > 0:
        sum += myDict[i]
        j += 1
    else:
        myDict[i] = myDict[i] * (-1)
if j != 0:
    myDict1["average_profit"] = sum // j
myList = [myDict, myDict1]
with open("text_77.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(myList))
