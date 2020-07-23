print("hi there!!")
num1 = int(input('enter no 1 :'))
num2 = int(input('enter no 2 :'))
sum = num1 + num2
print('your sum is',sum)


#currency converter


indr = input("enter your amount,(ex:10/-):")
indr_1 = float(indr)
indr_1 /= 75.49
print("the amount in Dollar is :",round(indr_1,2))

# value of (3x^3 - 2x^2 +3x -1)


x = input("enter the value of 'X' :")
x = float(x)
y = ((3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1)
print("y =", round(y,3))

#box by strings


print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 10, end = "")
print("+" + 10 * "-" + "+")

#_____time duration spend____


hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_m = (hour * 60) + mins #total minutes
dura_m = total_m + dura      #total minutes with duration time
total_h = dura_m // 60       #hour conversion of total minutes
while(total_h > 23):         #while loop to limit the hour between 0- 23
    total_h -= 24
else:
    pass
    
a_dura_m = dura_m % 60       #dividence is the required minutes 
print(total_h, ":", a_dura_m, sep='')
