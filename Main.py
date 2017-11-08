"""
Дан каталог книг. Про книгу известно: уникальный номер, автор, название, год издания.
Реализовать CRUD(создание-чтение-изменение-удаление), показ всех книг на экран и поиск по каждому из полей.
Учитывать, что каждое поле соответствует определенному типу данных.
"""

import json
import os

print('Приветствую!')
count = str(0)
print('В данной директории находятся файлы', os.listdir(path="."))
while count != 1:
    try:
        with open(input('введите имя каталога\n '), 'r+', encoding='utf-8') as data_file:
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
    with open(input('введите имя каталога\n '), 'r+', encoding='utf-8') as dataFile:
        data1 = json.load(dataFile)
        a = input('введите параметр поиска:\n ')
        for i in data1:
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
    with open(input('введите имя каталога, куда добавить книгу\n '), 'r+', encoding='utf-8') as jfr:
        jf_file = json.load(jfr)
        user_info = {'author': author, 'id': il, 'name': name, 'year': year}
        jf_file.append(user_info)
        print(jf_file)
    with open(input('введите имя каталога, подтвердив операцию\n '), 'r+', encoding='utf-8') as jfr:
        jfr.write(json.dumps(jf_file))
        jfr.close()





show_all_books()
search()
write_to_book(input('Введите автора: '), input('Введите идентификатор'),
              input('Введите название'), input('Введите дату'))
