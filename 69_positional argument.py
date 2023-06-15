# 1)
def cal(a, b, c) :
    print(a+b*c)

cal(45, 78, 5)
cal(78, 45, 5)


# 2)
def fun(a, b, c) :
    print(a, b, c)

fun(11, 22, 33)

# fun([11,22,33])  # fun() missing 2 required positional arguments : b and c

fun([10, 20, 30], [11, 12, 13], [22, 33, 44])

fun((), [], {})


# 3)
def fun() :
    print('hello python ! how are you ?')

fun()
# fun(11)  # typeError : fun() takes 0 positional arguments but 1 was given
