import calendar
# shoe date
c = calendar.TextCalendar(calendar.SUNDAY)
for i in c.itermonthdays(2020, 9):
    print(i)
# show month

for name in calendar.month_name:
    print(name)

print()

for day in calendar.day_name:
    print(day)
