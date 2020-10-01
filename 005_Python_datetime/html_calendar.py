import calendar

hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2020, 9)
print(st)
