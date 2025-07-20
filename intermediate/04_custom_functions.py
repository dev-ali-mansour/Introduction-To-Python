# Create a custom function to calculate the average value
def average(values):
    # Calculate the average
    average_value = sum(values) / len(values)

    # Round the results
    rounded_average = round(average_value, 2)

    # Return the rounded results
    return rounded_average


sales = [125.97, 84.32, 99.78, 154.21, 78.50, 83.67, 111.13]

# Calculating the average
print(average(sales))

# Storing average sales
average_sales = average(sales)
print(average_sales)
