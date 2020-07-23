number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))

larger_number = number1
if number2 > (larger_number): larger_number = number2
if number3 > (larger_number): larger_number = number3
if number4 > (larger_number): larger_number = number4
# print the result
print("The larger number is:", larger_number)
