import calendar
year = int(input("Enter year:"))
print(calendar.calendar(year, 1, 1, 6, 4))

'''
What are 1, 1, 6, and 4 here? The default parameters specified in the 'formatyear' method of the Calendar class are (theyear, w=2, l=1, c=6, m=3). Here,
w=column width of each date,
l=number of lines per week,
c=the no. of spaces between months,
and m=the number of months per row.
'''