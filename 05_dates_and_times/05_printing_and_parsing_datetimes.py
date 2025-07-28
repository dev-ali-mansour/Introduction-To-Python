from datetime import datetime

# Create datetime
dt = datetime(2017, 12, 30, 15, 19, 13)
print(dt.strftime("%Y-%m-%d"))
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
print(dt.strftime("%H:%M:%S on %Y/%m/%d"))
# ISO 8601 format
print(dt.isoformat())

# Parse a date string
dt = datetime.strptime("12/30/2017 15:19:13", "%m/%d/%Y %H:%M:%S")
print(type(dt))
print(dt)

# Incorrect format string
# dt = datetime.strptime("2017-12-30 15:19:13", "%Y-%m-%d") #ValueError: unconverted data remains:  15:19:13

# A timestamp
ts = 1514665153.0
# Convert to datetime and print
print(datetime.fromtimestamp(ts))
