
def rewrite_data():
    "осущ. перезапись в справочнике"
    data1 = input('введите данные которые нужно изменить :')
    
    data2 = input('введите данные которые нужно ввести :')
    
    with open('boock.txt', 'r', encoding='utf-8') as f:
        tel_boock = f.read()
    tel_boock = search2(tel_boock, data1, data2)
    
    with open('boock.txt', 'w', encoding='utf-8') as f:
        f.write('\n'([post for post in tel_boock]))
    print('Успешно')
    
def search2(boock: str, info1, info2) -> str:
    boock = boock.split()
    count = 0
    boock1 = [len(boock) / 3]
    n = 0
    Ni = ''
    for i in boock:
        
        count += 1
        if info1 in i:
            i = info2
        Ni += i
        if count % 3 == 0:
            boock1[n] == Ni
            if n < len(boock1)-1:
             n +=1  
    return boock1

def del_data():
    "осущ. удаление в справочнике"
    data1 = input('введите данные которые нужно удалить :')   
    
    with open('boock.txt', 'r', encoding='utf-8') as f:
        tel_boock = f.read()
    tel_boock = search_del(tel_boock, data1)
    
    with open('boock.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join([post for post in tel_boock]))
    print('Успешно')
    
def search_del(boock: str, info1) -> str:
    boock = boock.split()
    info_del = ""
    for i in boock:
        if info1 in i:
            i = info_del   
    return boock


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
