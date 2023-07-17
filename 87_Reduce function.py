# Reduce function
# Find the sum of all elements present inside list without using lambda.

from functools import reduce
def addall(x,y) :
    return x+y 
l = [10, 20, 30, 40, 50]
data = reduce(addall, l)
print(data)



# Find the sum of all elements present inside list with using lambda.

data = reduce(lambda x,y: x+y, l)
print(data)


# Find the product of all elements present inside list with using lambda.

l = [11, 22, 33, 44, 55]
data = reduce(lambda x,y: x*y, l)
print(data)


# Find the sum of all elements from 1 to 100.

data = reduce(lambda x,y: x+y, range(1,101))
print(data)


# Working with a list which is containing string data.

names= ['priyanka', 'rahul', 'zini', 'jack', 'scoot']
data = reduce(lambda x,y: x+y, names, 'welcome to codedais')
print(data)


# Working with dictionary.

d = {
    1:'priyanka',
    2:'rahul',
    3:'zini',
    4:'jack',
    5:'scoot'
}
data = reduce(lambda x,y: x+y, d.keys())
print(data)


# or,

d = {
    1:'priyanka',
    2:'rahul',
    3:'zini',
    4:'jack',
    5:'scoot'
}
data = reduce(lambda x,y: x+y, d.values())
print(data)


# Reduce vs Accumulate function :
# 1)

from itertools import accumulate
l = [1,2,3,4,5]
print(list(accumulate(l, lambda x,y: x+y)))

print(reduce(lambda x,y: x+y, l))


# 2)

from itertools import accumulate
l = [1,2,3,4,5]
print(list(accumulate(l, lambda x,y: x*y)))

print(reduce(lambda x,y: x*y, l))


