# The question is how many numbers have you hit in a lottery?

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits, "numbers are matched.")


# find the location of an element in the list--------------------------------------

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = int(input("enter the element you want to find: "))
found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")
