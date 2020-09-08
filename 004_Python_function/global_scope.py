def myFunction():

    global var1

    var = 2

    print("Do I know that variable?", var, var1)

    var1 += var



var1 = 1

myFunction()

print(var1)

# Using this keyword inside a function with the name (or names separated with commas) of a variable(s), 
# forces Python to refrain from creating a new variable inside the function 
# the one accessible from outside will be used instead.
