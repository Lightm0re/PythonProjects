def result():
    with open('text', 'r') as my_file:
        my_string = my_file.read()
        a = my_string.replace(' ', '')
        b = a.replace('.', '')
        count = b.replace('\n', '')
        letters = str(len(count)) + ' letters\n'
        words = str(len(my_string.split())) + ' words\n'
        lines = str(len(my_string.splitlines())) + ' lines\n'

    with open('result', 'w') as my_result:
        my_result.write(letters)
        my_result.write(words)
        my_result.write(lines)


result()
