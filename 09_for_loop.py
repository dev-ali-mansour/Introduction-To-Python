# Degrees list
degrees = [95.50, 73.25, 82.75, 59.5]

# Print each value in degrees
for degree in degrees:
    print(degree)

print("==================")

for degree in degrees:
    if degree >= 95:
        print("A+")
    elif degree >= 90:
        print("A")
    elif degree >= 85:
        print("B+")
    elif degree >= 80:
        print("B")
    elif degree >= 70:
        print("C+")
    elif degree >= 60:
        print("C")
    else:
        print("F")

print("==================")

# Looping through strings
name = "Cairo University"
for char in name:
    print(char)
