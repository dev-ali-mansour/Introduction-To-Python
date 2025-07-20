# Access information including the docstring
help(round)

# Access only the docstring
print(round.__doc__)


def average(values):
    # One-line docstring
    """Find the mean in a sequence of values and round to two decimal places."""
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average


# Access our docstring
print(average.__doc__)

# Update a function's doc
average.__doc__ = """Calculate the mean of values in a data structure, rounding the results to 2 digits."""


def average(values):
    # One-line docstring
    """
    Find the mean in a sequence of values and round to two decimal places.

    Args:
        values (list): A list of numeric values.

    Returns:
        rounded_average (float): The mean of values, rounded to two decimal places.
    """
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

# Help
help(average)