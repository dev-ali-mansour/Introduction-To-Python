from datetime import timedelta
import matplotlib.pyplot as plt

import pandas as pd

# Import W20529's ride in Q4 2017
rides = pd.read_csv('capital-onebike.csv',
                    parse_dates=['Start date', 'End date'])

# Create a duration column
rides['Duration'] = rides['End date'] - rides['Start date']

#  Average time out of the dock
print(rides['Duration'].mean())
print(rides['Duration'].median())

#  Total time out of the dock
print(rides['Duration'].sum())

# Percent of time out of the dock
print(rides['Duration'].sum() / timedelta(days=91))

# Count how many times the bike started at each station
print(rides['Member type'].value_counts())

# Percent of rides by member
print(rides['Member type'].value_counts() / len(rides))

# Add duration (in seconds) column
rides['Duration seconds'] = rides['Duration'].dt.total_seconds()
# Average duration per member type
print(rides.groupby('Member type')['Duration seconds'].mean())
# Average duration by month
print(rides.resample('ME', on='Start date')['Duration seconds'].mean())
# Size per group
print(rides.groupby('Member type').size())
# First ride per group
print(rides.groupby('Member type').first())

rides \
    .resample('ME', on='Start date') \
    ['Duration seconds'] \
    .mean() \
    .plot()
plt.show()

rides \
    .resample('D',on='Start date') \
    ['Duration seconds'] \
    .mean() \
    .plot()
plt.show()