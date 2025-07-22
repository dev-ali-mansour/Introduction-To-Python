# Populate a list with a for loop
nums = [12, 8, 21, 3, 16]
new_nums = []
for num in nums:
    new_nums.append(num + 1)
print(new_nums)

print("==================")

# A list comprehension
nums = [12, 8, 21, 3, 16]
new_nums = [num + 1 for num in nums]
print(new_nums)

print("==================")

# Nested Loop
paris_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        paris_1.append((num1, num2))
print(paris_1)

print("==================")

# Nested Loop with List Comprehension
paris_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
print(paris_2)

print("==================")

# Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, write a list
# comprehension that produces a list of numbers consisting of the squared values of i.
squared_numbers = [i ** 2 for i in range(0, 10)]
print(squared_numbers)

print("==================")
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0, 5)] for row in range(0, 5)]

# Print the matrix
for row in matrix:
    print(row)
