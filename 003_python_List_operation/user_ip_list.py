hatlist = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

print("existing hatlist:", hatlist)

# Step 1: write a line of code that prompts the user

user_input = int(input("enter the number: "))

# to replace the middle number with an integer number entered by the user.

hatlist[2] = user_input

print("\nNew hsatlist:", hatlist)

# Step 2: write a line of code here that removes the last element from the list.

del hatlist[-1]

# Step 3: write a line of code here that prints the length of the existing list.

print("\nLength after remove ",len(hatlist))

print("\nafter deleting the last element:", hatlist)
