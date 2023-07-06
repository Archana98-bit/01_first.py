# Nested function :
# 1)

def outer_fun() :
    print('i am inside outer fun')

    def inner_fun() :
        print('i am inside inner fun')


outer_fun()


# 2)

def outer_fun() :
    print('i am inside outer fun')

    def inner_fun() :
        print('i am inside inner fun')
        inner_fun()

outer_fun()



# 3)

def outer_fun() :
    print('i am inside outer fun')

    def inner_fun() :
        print('i am inside inner fun')


outer_fun()
# inner_fun()
