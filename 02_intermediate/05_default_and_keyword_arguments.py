# Positional arguments
# Round pit to 2 digits
print(round(3.14159265358, 2))

# Keyword arguments
# Round pi to 2 digits
print(round(number=3.14159265358, ndigits=2))


# Create a custom function with default arguments
def average(values, rounded=False):
    # Round average to two decimal plaaces if rounded is True
    if rounded == True:
        average_value = sum(values) / len(values)
        rounded_average = round(average_value, 2)
        return rounded_average
    else:
        average_value = sum(values) / len(values)
        return average_value


sales = [125.97, 84.32, 99.78, 154.21, 78.50, 83.67, 111.13]
# Get the average without rounding
print(average(sales, False))
# Get the average without rounding
print(average(sales))
# Get the average with rounding
print(average(values=sales, rounded=True))
