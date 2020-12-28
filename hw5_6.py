myDict = {}

for line in open("text_6.txt", "r", encoding="utf-8"):
    line = line.split()
    lectures = int(line[1][0:-3]) if line[1][0:-3].isdigit() else 0
    practics = int(line[2][0:-4]) if line[2][0:-4].isdigit() else 0
    labs = int(line[3][0:line[3].find('(')]) if line[3][0:line[3].find('(')].isdigit() else 0
    myDict[line[0]] = lectures + practics + labs
print(myDict)
