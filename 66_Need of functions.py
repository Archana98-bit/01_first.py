# Check whether a number is even or odd.
# 1)
a = 10
if a % 2 ==0 :
    print('Number is even')
else:
    print('Number is odd')

# 2)
b = 22
if b % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')

# 3)
c = 13
if c % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')


# Check whether the number is even or odd by using function.
# 1)

def evenodd(num):
    if num % 2 == 0:
        print('Even')

    else:
        print('Odd')

evenodd(10)
evenodd(67)
evenodd(80)


# Define user define function.
# def keyword is used to define function.
# 1)
def add(a,b,c) :
    print(a+b+c)

add(10,20,30)
add(68,97,39)


# 2)
def add(a,b,c) :
    '''this function is used to perform addition of three numbers '''
    print(a+b+c)

add(11,45,67)

print(add.__doc__)

print(len.__doc__)

print(input.__doc__)


# 3)
def add(a,b,c) :
    print('Inside function')
    print(a,b,c)

a,b,c = 23,45,89
add(a,b,c)

print('Outside function')
print(a,b,c)


# 4)
def add(x,y,z) :
    x = 1000
    print('Inside function')
    print(id(x))
    print(id(y))
    print(id(z))
    print(x,y,z)

a,b,c = 13,45,78
add(a,b,c)

print('Outside function')
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)


