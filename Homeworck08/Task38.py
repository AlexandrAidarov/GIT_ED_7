# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

import functions

while True:
    print("1.  вывод, 2. добавление, 3. поиск, 4. изменить, 5. удалить")
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.rewrite_data()
    else:
        break
    
    
# with open('boock.txt', 'w', encoding='utf-8') as f:
#     f.write('ФИО | номер телефона')


# with open('boock.txt', 'a', encoding='utf-8') as f:
#     f.write('\nФИО1 | номер телефона')

# with open('boock.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
        