# Allow any number of positional, non-keyword arguments
def average(*args):
    # Function code remains the same
    average_value = sum(args) / len(args)
    rounded_average = round(average_value, 2)
    return rounded_average


# Calculating across multiple lists
print(average(*[15, 29], *[4, 13], *[11, 8]))


# Use arbitrary keyword arguments
def average(**kwargs):
    average_value = sum(kwargs.values()) / len(kwargs.values())
    rounded_average = round(average_value, 2)
    return rounded_average


# Calling average with six kwargs
print(average(a=15, b=29, c=4, d=13, e=11, f=8))

# Calling average with one kwarg
print(average(**{"a": 15, "b": 29, "c": 4, "d": 13, "e": 11, "f": 8}))

# Calling average with three kwargs
print(average(**{"a": 15, "b": 29, **{"c": 4, "d": 13}, **{"e": 11, "f": 8}}))
