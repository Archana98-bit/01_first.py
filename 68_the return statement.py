# 1)
def fun(a) :
    print(a)
    return a*a


print(fun(15))


# 2)
def fun(a,b) :
    print(a,b)
    return a+b


print(fun(15,35))


# 3)
def fun(a,b) :
    print(a,b)
    return a+b


x = fun(15,35)
print(x)


# return list.
# 1)
def fun() :
    l = [10,20,30]
    return l

x = fun()
print(x)

for i in x:
    print(i)



# 2)
def fun() :
    t = (10,20,30)
    return t

x = fun()
print(x)

for i in x:
    print(i)


# 3)
def fun() :
    print('hello')
    return 10

print(fun())


# 4)
def fun() :
    print('good morning')
    print('good afternoon')
    return 20
    print('good evening')
    print('good night')

fun()


# 5)
def fun() :
    print('good morning')
    print('good afternoon')
    
    print('good evening')
    print('good night')
    return 67

fun()


# python function can return multiple value.
# 1)
def fun(a,b,c) :
    return a,b,c

print(fun(10,11,12))


# 2)
def fun(a,b,c) :
    return a*2,b*3,c*4

x, y, z = fun(10,11,12)

print(x,y,z)



# define a function, it will take 6 subject mark of a student 
# as an argument then return total mark and avg mark.

def cal(p,c,m,b,i,e) :
    tm = p+c+m+b+i+e
    print('total mark is ',tm)
    am = tm/6
    return am

print('avg mark is ', cal(34, 56, 78, 32, 90, 87))


# 2)
def cal(p,c,m,b,i,e) :
    tm = p+c+m+b+i+e
    am = tm/6
    return tm, am

print(cal(34, 56, 78, 32, 90, 87))


# 3)
def cal(p,c,m,b,i,e) :
    tm = p+c+m+b+i+e
    am = tm/6
    return tm, am

tm, am = (cal(34, 56, 78, 32, 90, 87))
print('total mark is ', tm)
print('avg mark is ', am)
