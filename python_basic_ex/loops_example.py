#loop with strings

spa = input("enter your game name")
if spa == 'Football':
 print("YES I lOve fOOtbbaalll...!")
elif spa == 'football':
 print("i want big FOOTBALLL..!")
else:
 print("HOLY Football! is not '", spa,"'.")


#tax calculator

income = float(input("Enter the annual income: "))
if income < 85528.0:
    tax = (income * (18 / 100)) - (556 + .002)
    if tax < 1:
        print("the tax is :", 0.0, "thalers")
    else:
        print("the tax is :", round(tax, 1), "thalers")
else:
    tax1 = (14839 + .002) + (85528 *(32/100))
    print("The tax is:", round(tax1, 1), "thalers")

#leap year or common year

year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("it's a common year.")
    elif year % 100 != 0:
        print("it's a leap year")
    elif year % 400 != 0:
        print("it's a common year.")
    else:
        print("it'leap year.")


