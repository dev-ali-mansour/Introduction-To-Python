import pandas as pd

# Import W20529's ride in Q4 2017
rides = pd.read_csv('capital-onebike.csv')
# See our data
print(rides.head(3))

print(rides['Start date'])
print(rides.iloc[2])

print('--------------------------')

# Loading datetimes with parse_dates
rides = pd.read_csv('capital-onebike.csv',
                    parse_dates=['Start date', 'End date'])
# Or:
rides['Start date'] = pd.to_datetime(rides['Start date'],
                                     format='%Y-%m-%d %H:%M:%S')
# Select Start date for row 2
print(rides['Start date'].iloc[2])

# Create a duration column
rides['Duration'] = rides['End date'] - rides['Start date']
# Print the first 5 rows
print(rides['Duration'].head(5))

print(rides['Duration'] \
      .dt.total_seconds() \
      .head(5))
