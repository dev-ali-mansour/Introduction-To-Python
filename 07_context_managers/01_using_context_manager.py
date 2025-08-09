with open('my_file.txt') as my_file:
    text = my_file.read()
    length = len(text)

print('The file is {} characters long.'.format(length))
