from datetime import datetime, timedelta, timezone

# US Eastern standard time zone
ET = timezone(timedelta(hours=-5))
# Timezone-aware datetime
dt = datetime(2017, 12, 30, 15, 9, 3, tzinfo=ET)
print(dt)

# India Standard time zone
IST = timezone(timedelta(hours=5, minutes=30))
# Convert to IST
print(dt.astimezone(IST))

# Adjusting timezone vs changing tzinfo
print(dt)
print(dt.replace(tzinfo=timezone.utc))
# Change original to match UTC
print(dt.astimezone(timezone.utc))
