from datetime import datetime, timedelta

# Create example datetimes
start = datetime(2017, 10, 8, 23, 46, 47)
end = datetime(2017, 10, 9, 0, 10, 57)

# Subtract datetimes to create a timedelta
duration = end - start
print(duration.total_seconds())

# Create a timedelta
delta1 = timedelta(seconds=1)
print(start)

# One second later
print(start + delta1)

# Create a one day and one second timedelta
delta2 = timedelta(days=1, seconds=1)
print(start)
print(start + delta2)

# Create a negative timedelta of one week
delta3 = timedelta(weeks=-1)
print(start)
# One week earlier
print(start + delta3)

# Same, but we'll subtract this time
delta4 = timedelta(weeks=1)
print(start)
# One week earlier
print(start - delta4)
