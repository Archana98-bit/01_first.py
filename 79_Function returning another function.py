# 1)

def outer() :
    print('hi outer')
    def inner() :
        print('hi inner')

    print('_____________')
    return inner

outer()


# 2)

def outer() :
    print('hi outer')
    def inner() :
        print('hi inner')

    print('_____________')
    return inner

x = outer()
x()
x()
x()


# 3)

def fun1(abc) :
    print('abc id is :', id(abc))
    return abc

def x() :
    print('x id is :', id(x))
    print('python....')

data = fun1(x)
print('data id is :', id(data))
data()
