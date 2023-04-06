# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


ListOfLetters = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

some_list = input("Введите стихотворение: ")
some_list = some_list.split()
print(some_list)
some_N = ""
num = 0
num2 = 0
nul = " "
for i in some_list:
    num = 0
    if some_list.index(i) == len(some_list) - 1:
        for x in i:
            if x in ListOfLetters:
                num += 1
        if num == num2:
            print("Парам пам-пам")
        elif num2 != num:
            print("Пам парам")
    else:
        for x in i:
            if x in ListOfLetters:
                num += 1
        if num2 == 0 or num == num2:
            num2 = num
        elif num2 != num:
            print("Пам парам")