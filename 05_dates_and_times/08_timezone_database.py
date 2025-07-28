from datetime import datetime
from dateutil import tz

# Eastern time
et = tz.gettz('America/New_York')

# Last ride
last = datetime(2017, 12, 30, 15, 9, 3, tzinfo=et)
print(last)
# First ride
first = datetime(2017, 10, 1, 15, 23, 25, tzinfo=et)
print(first)