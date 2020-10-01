import calendar

# create a plan text calender

c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2020, 9, 0, 0)
print(st)
