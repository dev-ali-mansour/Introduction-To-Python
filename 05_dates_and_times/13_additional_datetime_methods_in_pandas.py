import pandas as pd

# Import W20529's ride in Q4 2017
rides = pd.read_csv('capital-onebike.csv',
                    parse_dates=['Start date', 'End date'])

# Create a duration column
rides['Duration'] = rides['End date'] - rides['Start date']

print(rides['Duration'].dt.total_seconds().min())
print(rides['Start date'].head(3))
print(rides['Start date'].head(3) \
      .dt.tz_localize('America/New_York'))

# Try to set a timezone
# rides['Start date'] = rides['Start date'] \
#     .dt.tz_localize('America/New_York') # AmbiguousTimeError: Cannot infer dst time from 2017-11-05 01:56:50

# Handle ambiguous datetimes
rides['Start date'] = rides['Start date'] \
    .dt.tz_localize('America/New_York', ambiguous='NaT')

rides['End date'] = rides['End date'] \
    .dt.tz_localize('America/New_York', ambiguous='NaT')

# Re-calculate  duration, ignoring bad row
rides['Duration'] = rides['End date'] - rides['Start date']
# Find the minimum again
print(rides['Duration'].dt.total_seconds().min())

# Look at problematic row
print(rides.iloc[20])

# Year of the first three rows
print(rides['Start date'] \
      .head(3) \
      .dt.year)

# See weekdays for the first three rides
print(rides['Start date'] \
      .head(3) \
      .dt.day_name(locale='ar_EG.UTF-8'))

# Shift the indexes forward one, padding with NaT
print(rides['End date'].shift(1).head(3))
