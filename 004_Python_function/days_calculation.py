def isYearLeap(year):
    if year % 4 != 0:
        return False         # Function with one argument
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]     # Function with two arguments to return the total days of a given year, month
    res  = days[month - 1]
    if month == 2 and isYearLeap(year):
        res = 29
    return res


def dayOfYear(year, month, day):
    days = 0
    for m in range(1, month):
        md = daysInMonth(year, m)
        days += md

    md = daysInMonth(year, month)
    if (day >= 1 and day <= md):
        return days + day
    else:
        return None


testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]

for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    dy = testresults[i]
    print(yr,mo,"=",dy, "days","-> ",end="")
    result = daysInMonth(yr, mo)
    if result == testresults[i]:
        print("OK")
    else:
        print("Failed")


user = int(input("enter year: "))
user_1 = int(input("enter month number: "))
res_1 = daysInMonth(user,user_1)
print(res_1, "<- total days of the given month in the year")


user_2 = int(input("enter the year: "))
user_3 = int(input("enter the month: "))
user_4 = int(input("enter the day: "))
print(dayOfYear(user_2, user_3, user_4), "<- total number of days according to given data")
