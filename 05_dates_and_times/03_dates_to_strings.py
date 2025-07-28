from datetime import date

# Example date
d = date(2017, 11, 5)
# ISO format: YYYY-MM-DD
print(d)
# Express the date in ISO 8601 format and put it in as list
print([d.isoformat()])

# A few dates that computers once had trouble with
some_dates = ['2000-01-01', '1999-12-31']
# Print them in order
print(sorted(some_dates))

# Example date
d = date(2017, 1, 5)
print(d.strftime("%Y"))
# Format string with more text in it
print(d.strftime("Year is %Y"))
# Format: YYY/MM/DD
print(d.strftime("%Y/%m/%d"))
