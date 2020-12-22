from functools import reduce

my_func = lambda num1, num2: num1 * num2

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_func, my_list))
