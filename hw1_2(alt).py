secs = int(input("Введите количество секунд: "))
hrs = secs // 3600
secs = secs % 3600
mins = secs // 60
secs = secs % 60
print(f"{hrs:02}:{mins:02}:{secs:02}")