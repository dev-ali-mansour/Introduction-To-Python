from datetime import date

two_hurricanes = ["10/7/2016", "6/21/2017"]

# Create dates
two_hurricanes_dates = [date(2016, 10, 7), date(2017, 6, 21)]
print(two_hurricanes_dates[0].year)
print(two_hurricanes_dates[0].month)
print(two_hurricanes_dates[0].day)

# Finding the weekday of a date
print(two_hurricanes_dates[0].weekday())