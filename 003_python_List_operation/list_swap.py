myList = [10, 14, 12, 18, 57, 74, 47, 56, 1, 8, 3, 5]
length = len(myList)
print(myList)
for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print("after swap:\n", myList)
