data_1 = float(input("Enter your 1st value: "))
data_2 = float(input("enter your 2nd value: "))
data_3 = int(input("press 1 for add\npress 2 for sub\npress 3 for mul\npress 4 for div\n::::>"))
if data_3 == 1:
    print("the addition is ", data_1 + data_2)
elif data_3 == 2:
    print("The substraction is ", data_1 - data_2)
elif data_3 == 3:
    print("the multiplication is ", data_1 * data_2)
else:
    print("the substraction is ", data_1 / data_2)
    print("the divisor is ", data_1 % data_2)
