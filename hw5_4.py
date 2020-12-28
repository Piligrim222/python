myDict, myStr = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}, ""
with open("text_4.txt", "r", encoding="utf-8") as fr, open("text_4_0.txt", "w", encoding="utf-8") as fw:
    for line in fr:
        myStr += myDict[line.split("-")[0].rstrip()] + " - " + line.split("-")[1].strip() + "\n"
    fw.write(myStr.rstrip())
