# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
# import time
import random
x = int(input("Введите количество элементов в массиве: "))
some_list = [random.randint(1, 100) for _ in range(x)]
print(some_list)
number = int(input("Введите число: "))
difrens = some_list[0]
DifNum2 = some_list[0]
for i in range(x):
    DifNum = abs(number - some_list[i])
    
    if DifNum < difrens:
        TheNumber = some_list[i]
        difrens = DifNum
print(TheNumber)
        


# start = time.perf_counter()
# print(some_list.count(x))
# end = time.perf_counter()
# first = end - start