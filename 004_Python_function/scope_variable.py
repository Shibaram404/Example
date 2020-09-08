# a variable that exist outside of a function have a scope inside the function body
var = 2

def multByVar(x):
    return x * var

print(multByVar(7),"\n") 

## ....................

def mult(x):
    var = 5
    return x * var

print(mult(7),"\n")

### ...................

def multip(x):
    var = 7
    return x * var

var = 3
print(multip(7),"\n")

#### ..................

def adding(x):
    global var
    var = 7
    return x + var

print(adding(4))
print(var,"\n")

##### .................

var = 2
print(var)    # outputs: 2
                           # You can use the 'global' keyword followed by a variable name to make the variable's scope global,
def retVar():
    global var
    var = 5
    return var

print(retVar())    # outputs: 5

print(var,"\n") 

###### ..............

a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a,"\n")

####### ............

a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)

