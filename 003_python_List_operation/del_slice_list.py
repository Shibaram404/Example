myList = [10, 8, 6, 4, 2]
newList = myList[:]  # make a copy of the whole list
print(newList)

#

myList = [10, 8, 6, 4, 2]
del myList[1:3]  # removing a slice from the list but slice doesn't produce any new list
print(myList)

##

myList = [10, 8, 6, 4, 2]
del myList[:]   # removing the whole list
print(myList)

###

myList = [10, 8, 6, 4, 2]
myList = newList  ##  without slice '[:]'
del myList         #  The del instruction will delete the list itself, not its content.
print(newList)
## print(myList) it's give an error of 'name is not defind'
