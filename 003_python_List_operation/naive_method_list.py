myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

newList = []

for number in myList:               # naive method

    if number not in newList:       # way to remove duplicate from list

        newList.append(number)

    

print("The list with unique elements only:")

print(newList)
