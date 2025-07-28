from datetime import datetime, timezone, timedelta
from dateutil import tz

spring_ahead_159am = datetime(2017, 3, 12, 1, 59, 59)
print(spring_ahead_159am.isoformat())
spring_ahead_3am = datetime(2017, 3, 12, 3, 0, 0)
print(spring_ahead_3am.isoformat())
print((spring_ahead_3am - spring_ahead_159am).seconds)

EST = timezone(timedelta(hours=-5))
EDT = timezone(timedelta(hours=-4))
spring_ahead_159am = spring_ahead_159am.replace(tzinfo=EST)
print(spring_ahead_159am.isoformat())
spring_ahead_3am = spring_ahead_3am.replace(tzinfo=EDT)
print(spring_ahead_3am.isoformat())
print((spring_ahead_3am - spring_ahead_159am).seconds)

# Create eastern timezone
eastern = tz.gettz('America/New_York')
# 2017-03-12 01:59:59 in eastern time (EST)
spring_ahead_159am = datetime(2017, 3, 12, 1, 59, 59,
                              tzinfo=eastern)

# 2017-03-12 03:00:00 in eastern time (EDT)
spring_ahead_3am = datetime(2017, 3, 12, 3, 0, 0,
                            tzinfo=eastern)
