# Recall list comprehensions
nums = [2 * num for num in range(10)]
print(nums)

print("=======================")

# Use () instead of [] to create a generator expression
nums = (2 * num for num in range(10))
print(nums)

print("=======================")

# Printing values from a generator
result = (num for num in range(6))
for num in result:
    print(num)

print("=======================")

# Lazy evaluation means that the values are generated on-the-fly, not stored in memory
result = (num for num in range(6))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

print("=======================")

# Generators can handle large data sets without consuming too much memory
# nums = [num for num in range(10**1000000)] # Don't do this, it will crash your computer!
nums = (num for num in range(10 ** 1000000))  # This is fine, it uses a generator
print(next(nums))
print(next(nums))
print(next(nums))

print("=======================")

# Conditionals in generator expressions
even_nums = (num for num in range(10) if num % 2 == 0)
print(list(even_nums))

print("=======================")


# Build a generator function
def num_sequence(n):
    """Generate vales from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1


result = num_sequence(5)
print(type(result))
print(list(result))

print("========================")

# Create a generator object that will produce values from 0 to 30. Assign the result to result and use num as the iterator variable in the generator expression.
# Print the first 5 values by using next() appropriately in print().
# Print the rest of the values by using a for loop to iterate over the generator object.

# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)


