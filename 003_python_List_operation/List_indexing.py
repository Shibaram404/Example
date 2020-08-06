numbers = [10, 5, 7, 2, 1]

print("Original list content:", numbers) # printing original list content



numbers[0] = 111

print("\nAfter replacing with 1st element", numbers) # printing previous list content



numbers[1] = numbers[4] # copying value of the fifth element to the second

print("\ncopy the 5th element into 2nd", numbers) # printing previous list content



print("\nList length:", len(numbers)) # printing the list's length

print("\n3rd element:", numbers[2])


del numbers[1] # removing the second element from the list

print("\nNew list's length after remove the 2nd element:", len(numbers)) # printing new list length

print("\nNew list content:", numbers) # printing current list content


# negative indices

numbers = [111, 7, 2, 1]

print(numbers[-4])

print(numbers[-1])

print(numbers[-2])
