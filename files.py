import re


def result():
    try:
        with open('text', 'r') as my_file:
            my_string = my_file.readlines()
            lines = words = letters = 0
    except FileNotFoundError:
        print('Потерял файл, тоби п**да, тикай с села')
    else:
        for i in my_string:
            lines += 1
            for j in i.split():
                words += 1
            for j in re.sub(r'\W', '', i):
                letters += 1
        with open('result', 'w') as my_result:
            my_result.write(str(lines)+' lines\n')
            my_result.write(str(words)+' words\n')
            my_result.write(str(letters)+' letters\n')
            my_result.close()


result()
