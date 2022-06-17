import calendar

year = 2022
month = 6

# display the calendar
print(calendar.month(year, month))

# create a plain text calendar
c = calendar.TextCalendar(calendar.WEDNESDAY)
str = c.formatmonth(year, month, 0, 0)
print(str)