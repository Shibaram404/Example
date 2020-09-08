## Finding Largest element from the List



# 1st way----------------------------------------------

myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]

largest = myList[0]



for i in myList:

    if i > largest: # performs one unnecessary comparison, when the first element is compared with itself

        largest = i



print(largest)



# 2nd way----------------------------------------------

myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]

largest = myList[0]



for i in range(1, len(myList)):   # by define the range using len function omit 1st element

    if myList[i] > largest:

        largest = myList[i]



print(largest)



# 3rd way-----------------------------------------------

myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]

largest = myList[0]



for i in myList[1:]:   # by slicing the list ignore the 1st element

    if i > largest:

        largest = i



print(largest)
