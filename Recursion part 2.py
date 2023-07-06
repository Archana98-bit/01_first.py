# Factorial of a number by using recursion.

def fact(num) :
    if num == 1 :
        return 1
    return num*fact(num-1)

print(fact(6))



# Fibonacci series by using recursion.

def fib(num) :
    if num <= 1 :
        return num
    else :
        return fib(num-1) + fib(num-2)       # binary recursion
    
print(fib(3))
