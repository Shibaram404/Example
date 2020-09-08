twos = [2 ** i for i in range(8)]  # list comprehension examples:
print(twos)

squares = [x ** 2 for x in range(10)]
print(squares)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)
