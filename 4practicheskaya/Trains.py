"""Создайте класс с именем train, содержащую поля: название пункта назначения, номер поезда, время отправления.
Ввести данные в массив из пяти элементов типа train, упорядочить элементы по номерам поездов. Добавить возможность
вывода информации о поезде, номер которого введен пользователем. Добавить возможность сортировки массив по пункту
назначения, причем поезда с одинаковыми пунктами назначения должны быть упорядочены по времени отправления. """
from operator import attrgetter
from datetime import datetime


class Train:
    def __init__(self, name, number, date):
        self.name = name
        self.number = number
        self.date = date

    def __repr__(self):
        return repr((self.name, self.number, self.date))


# Создание массива элементов
mass = []
for i in range(5):
    new_element = Train(input('Введите пункт назначения'), int(input('Введите номер поезда')),
                        input('Введите время отправления'))
    mass.append(new_element)
sorted_mass = sorted(mass, key=lambda train: train.number)
print(sorted_mass)
# Вывод информации
info = input('Введите номер поезда')
for i in mass:
    if int(info) == i.number:
        tru_time = datetime.strptime(i.date,'%H%M')
        print('Поезд с пунктом назначения', i.name, 'c номером', i.number, 'отправляется в ', tru_time)
# Сортировка по пункту назначения + время отправления
new_sorted_mass = sorted(mass, key=attrgetter('name', 'date'))
print(new_sorted_mass)
