# Local variable :

def fun1() :
    a = 22        # local variable
    print(a)

def fun2() :
    print(a)

fun1()
fun1()



# Global variables :

a = 11         # Global variable
def fun() :
    print(a)


def fun2() :
    print(a)

fun()
fun2()

# 2)

a = 10
def fun() :
    print(a)


def fun2() :
    print(a)

fun()
fun2()
print(a)

