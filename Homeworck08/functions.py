
def rewrite_data():
    "осущ. перезапись в справочнике"
    data1 = input('введите данные которые нужно изменить :')
    
    data2 = input('введите данные которые нужно ввести :')
    
    with open('boock.txt', 'r', encoding='utf-8') as f:
        tel_boock = f.read()
    tel_boock = search2(tel_boock, data1, data2)
    
    with open('boock.txt', 'w', encoding='utf-8') as f:
        f.write(tel_boock)
    print('Успешно')
    
def search2(boock: str, info1, info2) -> str:
    boock = boock.split()
    boock1 = ""
    for i in boock:
        if info1 in i:
            i = info2
        boock1 += i    
    return boock1




def show_data():
    "выводит информацию из справочника"
    with open('boock.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    

def add_data():
    "добавляет информацию в справочник"
    fio = input('введите ФИО :')
    fone_number = input('введите телефон')
    with open('boock.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {fone_number}')
    print('Успешно!')


def find_data():
    "осущ. поиск в справочнике"
    data = input('введите данные для поиска :')
    with open('boock.txt', 'r', encoding='utf-8') as f:
        tel_boock = f.read()
    print('Результат поиска:')
    print(search(tel_boock, data))

def search(boock: str, info) -> str:
    boock = boock.split('\n')
    return '\n'.join([post for post in boock if info in post])
