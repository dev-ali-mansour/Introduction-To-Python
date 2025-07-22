# Conditional in comprehensions
nums = [num ** 2 for num in range(10) if num % 2 == 0]
print(nums)

print("=======================")

nums = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(nums)

print("=======================")

# Dictionary Comprehensions
pos_neg = {num: -num for num in range(9)}
print(pos_neg)
print(type(pos_neg))

print("=======================")

# You are given a list of strings fellowship and, using a list comprehension, you will create a list that only
# includes the members of fellowship that have 7 characters or more.

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)

print("=======================")

# You will work on the same list, fellowship and, using a list comprehension and an if-else conditional statement in the
# output expression, create a list that keeps members of fellowship with 7 or more characters and replaces others with
# an empty string. Use member as the iterator variable in the list comprehension.

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]

# Print the new list
print(new_fellowship)

print("=======================")
