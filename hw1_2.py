secs = int(input("Введите количество секунд: "))
hrs = secs // 3600
secs = secs - hrs * 3600
mins = secs // 60
secs = secs - mins * 60
if mins < 10:
    mins = "0" + str(mins)
if hrs < 10:
    hrs = "0" + str(hrs)
if secs < 10:
    secs = "0" + str(secs)
print(str(hrs) + ":" + str(mins) + ":" + str(secs))
