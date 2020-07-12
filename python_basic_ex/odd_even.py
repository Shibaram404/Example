odd_number = 0
even_number = 0

number = int(input("Enter a number or type 0 to stop: "))

while number != 0:
    if number % 2 != 0:
        odd_number += 1
        number = sav
    else:
        even_number += 1
    number = int(input("Enter a number or type 0 to stop: "))

print("Odd numbers count:", odd_number)
print("Even numbers count:", even_number)

