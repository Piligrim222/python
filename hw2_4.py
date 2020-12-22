inp = "jkfkf hg f kj gkjffkgjjkvghfgvkvf gfk,g kj f j"
my_list = input("Печатать сюда: ").split()
for i in range(len(my_list)):
    print(f"{i + 1}. {my_list[i][:10]}")
print("Спасибо!")
