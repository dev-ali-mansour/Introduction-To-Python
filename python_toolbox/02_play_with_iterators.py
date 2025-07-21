avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers)
print(type(e))

e_list = list(e)
print(e_list)

print("==================")

for index, value in enumerate(avengers):
    print(index, value)

print("==================")

for index, value in enumerate(avengers, start=10):
    print(index, value)

print("==================")

avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']
z = zip(avengers, names)
print(type(z))

z_list = list(z)
print(z_list)

print("==================")

for z1,z2 in zip(avengers, names):
    print(z1,z2)

print("==================")

avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']
z = zip(avengers, names)
print(*z)