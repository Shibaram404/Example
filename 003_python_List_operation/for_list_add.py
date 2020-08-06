myList = [10, 1, 8, 3, 5]

total = 0



for i in range(len(myList)):

    total += myList[i]



print(total)


###  without len() function


myList = [10, 1, 8, 3, 5]
total = 0

for i in myList:
    total += i

print(total)
