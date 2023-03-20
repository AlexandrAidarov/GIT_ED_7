# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
#  не превосходящие числа N.


N = int(input("Введите число N: "))
sum = 2
# number = 1
if sum <= N:
    print(sum)
    while sum < N:
        sum = sum * 2
        if sum < N:
            print(sum)
        # number = number + 1

else :
    print("не верное значение")