secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
num = int(input("enter your guessed integer number :"))
while num != secret_number:
    print("Ha ha ! You are stuck in my loop!")
    num = int(input("enter your guessed integer number :"))
else:
    print("well done, muggle! You are free now.")
    print(secret_number)
