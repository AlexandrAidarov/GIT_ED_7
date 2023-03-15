# 4 Определить число введено.

number = int(input("Введите число: "))

if number % 2 == 0 and number < 0:
     print("Отрицательное четное число")
elif number == 0: 
    print("Ноль")
elif number % 2 != 0 and number < 0:
     print("Отрицательное нечетное число")
elif number % 2 == 0 and number > 0:
     print("Положительное четное число")
elif number % 2 != 0 and number > 0:
     print("Положительное нечетное число")