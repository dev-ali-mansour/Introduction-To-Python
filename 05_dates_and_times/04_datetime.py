from datetime import datetime

# dt = datetime(2017, 10, 1, 15, 23, 25, 500000)
dt = datetime(year=2017, month=10, day=1,
              hour=15, minute=23, second=25, microsecond=500000)
print(dt)

dt_hr = dt.replace(minute=0, second=0, microsecond=0)
print(dt_hr)

