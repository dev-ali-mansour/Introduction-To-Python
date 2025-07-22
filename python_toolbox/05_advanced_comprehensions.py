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
