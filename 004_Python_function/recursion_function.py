def fib(n):
    if n < 1:                  #fibonaki
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
    
def factorialFun(n):
    if n < 0:
        return None          #factorial
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

for n in range(1, 10):
    print(n, "fibonaki->", fib(n), "factorial->", factorialFun(n))
    

# recursion is a technique where a function invokes itself
# for recursion there must have to be a base function to break the loop
