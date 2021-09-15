# modules_datetime.py

from datetime import datetime

# Create a date time using year, month, day as arguments
birthday = datetime(1984, 6, 27, 23, 11)
print(birthday)
print(birthday.year)

# Weekday output:
# 0 represents Monday
print(birthday.weekday())

# Current Time
current_time = datetime.now()
print(current_time)

# date arithmatic

date_difference = datetime(2018, 1, 1) - datetime(2017, 1, 1)
print(date_difference)

wedding_date = datetime(2014, 10, 14)

time_married = datetime.now() - wedding_date

print(time_married)

# parse dates

parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')

print(parsed_date.year)

date_string = datetime.strftime(datetime.now(), '%B %d %y')
print(date_string)