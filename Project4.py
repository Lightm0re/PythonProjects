'''Дан список результатов попыток одного спортсмена для некоторого соревнования.

Написать функцию, которая считает сколько за сессию был установлен новый рекорд, т.е. текущее значение превышает значение максимального.

Например

Имеем список результатов.:

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1].

В данном случае ответ: 2.'''


def adds():
    scores = input("Введите список результатов:").split(' ')
    print('Список результатов \n', scores)
    count = 0
    rec = scores[0]
    for ind, el in enumerate(scores):
        if int(el) > int(rec):
            rec = el
            count += 1
    return 'Количество рекордов:', count


print(adds())





