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

print("==================")

# Loop through dictionaries
books = {"Ahmed Ali": "Introduction To Python", "Sara Saad": "Fundamentals Of Artificial Intelligence",
         "Ali Mansour": "Fundamentals Of Machine Learning"}
for key, val in books.items():
    # print(key,val)
    print(key, "=>", val)

print("==================")

# Loop through range
for i in range(1, 5):
    print(i)

print("==================")

# Building a counter
# No Cars yet
cars = 0
# Loop through numbers 1-8
for i in range(1, 9):
    # Add one car during each iteration
    cars += 1  # Same as cars = cars + 1

print(cars)
