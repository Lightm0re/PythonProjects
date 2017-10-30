import re


def result():

    try:
        with open('text', 'r') as my_file:
            my_string = my_file.read()
    except FileNotFoundError:
        print('Тоби пизда, тика с села')
    else:
            strings = re.sub(r'\W', '', my_string)
            letters = str(len(strings)) + ' letters\n'
            words = str(len(my_string.split())) + ' words\n'
            lines = str(len(my_string.splitlines())) + ' lines\n'
            with open('result', 'w') as my_result:
                my_result.write(letters)
                my_result.write(words)
                my_result.write(lines)
                my_result.close()


result()
