"""
Дан каталог книг. Про книгу известно: уникальный номер, автор, название, год издания.
Реализовать CRUD(создание-чтение-изменение-удаление), показ всех книг на экран и поиск по каждому из полей.
Учитывать, что каждое поле соответствует определенному типу данных.
"""

import json
import codecs
count = str(0)
while count != 1:
    try:
        with open(input('введите имя каталога\n '), 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        print('Вы ввели несуществующий каталог\n')
        count = str(1)
    else:
        count = str(0)
        break


def show_all_books():
    for i in data:
        print('Книга:', i)


def open_catalog():
    with open(input('введите имя каталога\n '), 'r', encoding='utf-8') as data_file:
        data = json.load(data_file)
        a = input('введите параметр поиска:\n ')
        for i in data:
            print(i.get(a))


def search():
    b = str(0)
    while b != 1:
        try:
            open_catalog()
        except FileNotFoundError:
            print('Вы ввели несуществующий каталог\n')
            open_catalog()
        finally:
            b = input('Завершить поиск по полям?:\nНажмите "1" для завершения, для продолжения поиска нажмите Enter \n')
            if b == '1':
                break


def write_to_book(author, il, name, year):
    jf_file = json.load(data)
    with open(data, 'w',encoding='utf-8') as jf:
        jf_target = list(jf_file)
        print(jf_target)
        user_info = {'author': author, 'id': il, 'name': name, 'year': year}
        jf_target.append(user_info)
        json.dump(jf_file, jf, indent=4)


#show_all_books()
#search()
write_to_book('1','2','3','4')
