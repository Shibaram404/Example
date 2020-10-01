from datetime import *

# get today's date
# * indicate import all
# never ever give the same name as python module name

toDay = date.today()
print("Today's date is ", toDay)

# print out date's individual components

print("Date's components: ", toDay.day, toDay.month, toDay.year)

# retrieve toda's weekday (0 = Monday, 6 = Sunday)

print("Today's weekday is:", toDay.weekday())
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("which is", days[toDay.weekday()], "Day")

# today's date & time

today1 = datetime.now()
print("now the time & date is: ", today1)

# only time

t = datetime.time(datetime.now())
print("The time is:", t)
