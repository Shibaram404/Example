from datetime import *

# construct a basic timedelta

print(timedelta(days=365, hours=5, minutes=1))

# print today's date

new = datetime.date(datetime.now())

print("today is: " + str(new))

# print today's date one year from now

print("one year from now it will be: " + str(new + timedelta(days=365)))

# create a timedelta that uses more than one arguments
# find the date
day = int(input("enter the number of days: "))
week = int(input("enter the number of weeks: "))
print("In", day, "days and", week, "weeks, It will be " + str(new + timedelta(days=day, weeks=week)))

# calculate the date 1 week ago

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %y")
print("One week ago it was: " + str(s))

# how many days till April fool day

toDay = date.today()
afd = date(toDay.year, 4, 1)

# if the day has already gone use replace function to get the date for next year

if afd < toDay:
    print("April Fool's day went by %d days ago" % ((toDay - afd).days))
    afd =afd.replace(year = toDay.year+1)
# now calculate the amount of time untill April fool's day

time_to_afd = afd - toDay
print("It's just ", time_to_afd.days, "days untill April Fool's Day")

