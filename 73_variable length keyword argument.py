# variable length keyword argument.
# 1)

def fun(**a) :
    print(a)

fun()


# 2)

def fun(**a) :
    print(a)

fun(x=11, y=99, z=[10, 20, 30])


# 3)

def fun(x, **a) :
    print(a)
    print(x)

fun(x=10, a=20, b=30, c=40)


# 4)

def fun(x, *z, **a) :
    print(x)
    print(z)
    print(a)

fun(99, 88, 77, a=11, b=22, c=33)


# 5)

def fun(**a) :
    print(a)

fun(a={})


# 6)

def fun(*a, **b) :
    print(a)
    print(b)

fun()


# 7)

def fun(*a, **b) :
    print(a)
    print(b)

fun(x=11, y=22)

