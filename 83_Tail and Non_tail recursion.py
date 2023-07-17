# non-tail recursion
# 1)

def fun(num) :
    if num == 4 :
        return
    
    else :
        print(num)
        fun(num+1)

fun(1)

# 2)

def fun(num) :
    if num == 4 :
        return
    
    else :
        fun(num+1)
        print(num)

fun(0)


# 3)

def fun(num) :
    if (num > 0) :
        print(num)
        fun(num-1)
        fun(num-1)

fun(3)


# 4)

def fun(num) :
    if (num > 100) :
        return num-10
    return fun(fun(num+11))

d = fun(97)
print(d)
