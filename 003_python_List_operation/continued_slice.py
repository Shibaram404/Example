myList = [10, 8, 6, 4, 2]  

 # myList[:end]
 # is a more compact equivalent of:
 # myList[0:end]

newList = myList[:3]
print(newList)

###

myList = [10, 8, 6, 4, 2]
newList = myList[3:]
print(newList)

 # Similarly, if you omit the end in your slice, it is assumed that you want the
 ## slice to end at the element with the index len(myList)
 ### myList[start:len(myList)]
