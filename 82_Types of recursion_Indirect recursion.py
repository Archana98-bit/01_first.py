# Indirect Recursion :
# 1)

def fun1(num) :
    if num <= 6 :
        print(f'fun1 = {num*2}')
        fun2(num+1)

    return


def fun2(num) :
    if num <= 6 :
        print(f'fun2 = {num*100}')
        fun1(num+1)

    return 

fun1(1)


# 2)

def fun1(i) :
    if i<0 :
        return fun2(i-1)
    return "0"

def fun2(i) :
    if i>0 :
        return fun1(i-1)
    return "1"

print(fun1(29))
