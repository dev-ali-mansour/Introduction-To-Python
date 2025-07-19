# Printing
print("Display this as an output on the screen")

# Checking data types
print(type(print))

# Looping through a range of numbers
for num in range(1, 5):
    print(num)

sales = [125.97, 84.32, 99.78, 154.21, 78.50, 83.67, 111.13]
# Find the largest sale
print(max(sales))

# Find the smallest sale
print(min(sales))

# Store Total sales
total_sales = sum(sales)

# Round to two decimal places
round(total_sales, 2)
print(total_sales)

# Store total sales using nested functions
total_sales = round(sum(sales), 2)
print(total_sales)

# Count the number of elements
print(len(sales))

# Calculate average sales
print(sum(sales) / len(sales))

# Length of a string
print(len("Introduction to Programming for Developers"))

# Length of dictionary
print(len({"a": 1, "b": 2, "c": 3}))

# Sort the sales list in ascending order
print(sorted(sales))

# Sort a sting alphabetically
print(sorted("George"))

# Get information about the sorted() function
help(sorted)

# Find total sales
# Crearte a variable to increment

sales_count = 0

# Loop through sales
for sale in sales:
    # Increment sales_count by each sale
    sales_count+=sale
    print(sales_count)
