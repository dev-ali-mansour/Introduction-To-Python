from datetime import date
from datetime import timedelta

# Example numbers
a = 11
b = 14
l = [a, b]

# Find the least number in the list
print(min(l))

# Subtract two numbers
print(b - a)

# Add 3 to a
print(a + 3)

# Create two dates
d1 = date(2017, 11, 5)
d2 = date(2017, 12, 4)
l = [d1, d2]

# Print the minimum date
print(min(l))

# Subtract two dates
delta = d2 - d1
print(delta.days)

# Create a 29 timedelta
td = timedelta(days=29)
print(d1 + td)
