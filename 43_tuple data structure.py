# Creation of empty tuple :

t = ()
print(t)
print(type(t))


# Creation of single value tuple :

t = (23,)
print(t)
print(type(t))


# 1)
t = (23)    # without comma
print(t)     # 23
print(type(t))   # <class 'int'>


# 2) Creation of tuple with different data items.

t = (55, 'priyanka', 554.89, False)
print(t)
print(type(t))


# Creation of tuple without using () .

t = 10, 20, 78, 'priyanka', 989.07, True
print(t)
print(type(t))


# Creation of tuple using tuple() .

l = [10, 30, 60, 'priyanka', 'rahul', True]
t = tuple(l)    # list to tuple
print(t)


# 2)
t = tuple(range(21))
print(t)


# 3)
t = tuple('priyanka')
print(t)


# tuple packing and unpacking concept.
# tuple packing :

a = 21
b = 45
c = 89
d = 'priyanka'
e = True
t = a, b, c, d, e    # packing
print(t)


# tuple unpacking :

t = (34, 56, 'priyanka', 45.90, False)
a, b, c, d, e = t
print(a, b, c, d, e)


# functions in tuple.

def fun() :
    l = [23, 56, 78, 89, 80]
    return(l[3], l[4], l[1])

t = fun()
print(t)


# nested tuple.
# 1)
t = ((45, 'priyanka', 89.9), (56, 'rahul', 56.8))
print(t[1])
print(t[0][1])


# 2)
t = ((34, 'priyanka', 98.09), ('rahul', 90, 56.45))

for i in t:
    print(i)


# 3)
t = ((45, 'susmita', 67.90), [56, 'debasish', 90.8])
t[1][1] = 'subha'
print(t)
