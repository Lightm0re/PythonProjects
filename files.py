def result():
    with open('text', 'r') as my_file:
        my_string = my_file.read()
        count = 0
        for i, j in enumerate(my_string):
                if j != ' ' and j != '.':
                    count += 1
        words = str(len(my_string.split())) + ' words'
        lines = str(len(my_string.splitlines())) + ' lines'
        letters = str(count) + ' letters'
    with open('result', 'w') as my_result:
        my_result.write(letters)
        my_result.write('\n')
        my_result.write(words)
        my_result.write('\n')
        my_result.write(lines)
        my_result.write('\n')


result()
