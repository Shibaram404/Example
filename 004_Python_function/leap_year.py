def isYearLeap(testData):     
    if (testData) % 4 == 0:
        return True
    else:
        False

# testing code to know my function work properly

testData = [2021, 2000, 2016, 1987]
testResults = [True, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end=" ")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
		
# # user input to know Leap year

year = int(input("Enter your year: "))
res = isYearLeap(year)
print(res,"->", end = "")
if res == True:
    print("This is leap year.")
else:
    print("This is not a leap year.")

