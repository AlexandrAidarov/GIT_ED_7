# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
x = int(input("Введите количество элементов в массиве: "))
some_list = [random.randint(1, 100) for _ in range(x)]
print(some_list)

minNum = int(input("Введите минимальное число: "))
maxNum = int(input("Введите минимальное число: "))
for i in range(len(some_list)):
    if minNum <= some_list[i] <= maxNum:
        print(i)


