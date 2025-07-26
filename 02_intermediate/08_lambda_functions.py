# Lambda average function
lambda x: sum(x) / len(x)

# Get the average
print((lambda x: sum(x) / len(x))([3, 6, 9]))

# Store lambda function in a variable
average = lambda x: (sum(x) / len(x))

# Call the average function
print(average([3, 6, 9]))

# Lambda function with two arguments
print((lambda x, y: x ** y)(2, 3))

names = ["john", "sally", "leah"]
# Apply a lambda function inside map()
capitalize = map(lambda x: x.capitalize(), names)
print (capitalize)
# Convert to list
print(list(capitalize))