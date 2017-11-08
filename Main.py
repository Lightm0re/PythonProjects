"""
Дан каталог книг. Про книгу известно: уникальный номер, автор, название, год издания.
Реализовать CRUD(создание-чтение-изменение-удаление), показ всех книг на экран и поиск по каждому из полей.
Учитывать, что каждое поле соответствует определенному типу данных.

В программе реализован небольшой графический интерфейс для быстрого выбора нужных операций.
После нажатия кнопки, ввод данных производится в меню запуска.
"""

import json
from tkinter import *


def show_all_books():
    count = str(0)
    while count != 1:
        try:
            books = json.load(open(input('введите имя каталога\n '), 'r+', ))
            for i, b in enumerate(books):
                print('Книга:', str(i), b)
        except FileNotFoundError:
            print('Вы ввели несуществующий каталог\n')
            count = str(1)
        else:
            break


def open_catalog():
    books = json.load(open(input('введите имя каталога\n '), 'r+', ))
    a = input('введите параметр поиска:\n ')
    print('Книги по полю -', str(a))
    for i in books:
        print(i.get(a))


def search():
    b = str(0)
    while b != 1:
        try:
            open_catalog()
        except FileNotFoundError:
            print('Вы ввели несуществующий каталог\n')
        else:
            b = input('Завершить поиск по полям?:\nНажмите "1" для завершения, для продолжения поиска нажмите Enter \n')
            if b == '1':
                break


def write_book(author, il, name, year):
    with open(input('введите имя каталога, куда добавить книгу\n '), 'r') as jfr:
        jf_file = json.load(jfr)
        user_info = {'author': author, 'id': il, 'name': name, 'year': year}
        jf_file.append(user_info)
        print(jf_file)
    with open(input('повторите имя каталога, подтвердив операцию\n '), 'r+') as jfr:
        jfr.write(json.dumps(jf_file))
        jfr.close()


def delete_book():
    data = json.load(open(input('введите имя каталога\n '), 'r', ))
    b = input('введите номер книги по порядку')
    del data[int(b)]
    print(data)
    with open(input('повторите имя каталога, подтвердив операцию\n '), 'w') as jfr:
        jfr.write(json.dumps(data))
        print(data)
        jfr.close()


def change_book():
    data = json.load(open(input('введите имя каталога\n '), 'r', ))
    b = input('введите номер книги по порядку')

    a = dict(data[int(b)])
    print(a)
    d = input('введите параметр изменения')
    if a.get(str(d)):
        a[d] = input('введите новое значение')
        print(a)
    with open(input('повторите имя каталога, подтвердив операцию\n '), 'w') as jfr:
        data.insert(int(b), a)
        data.remove(data[int(b) + 1])
        jfr.write(json.dumps(data))
        jfr.close()


def button_write_book():
    write_book(input('Введите автора: '), input('Введите идентификатор'),
               input('Введите название'), input('Введите дату'))


root = Tk()
root.title("Каталог книг")
root.geometry("300x250")
main_menu = Menu()
clicks = 0
btn = Button(text="Показать все книги в каталоге", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=show_all_books)
btn.pack()
btn = Button(text="Поиск по параметрам", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=search)
btn.pack()
btn = Button(text="Удалить книгу", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=delete_book)
btn.pack()
btn = Button(text="Добавить книгу", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16",
             command=button_write_book)
btn.pack()
btn = Button(text="Изменить книгу", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16",
             command=change_book)
btn.pack()
root.config(menu=main_menu)
root.mainloop()

