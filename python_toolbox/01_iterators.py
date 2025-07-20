word = 'Da'
it = iter(word)
print(next(it))
print(next(it))
# print(next(it)) # Raises StopIteration error

word = 'Data'
it = iter(word)
print(*it)

file =open('file.txt')
it = iter(file)
print(next(it))
print(next(it))