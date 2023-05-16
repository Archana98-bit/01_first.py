# 1)
l = [i for i in range(11)]
print(l)


# 2)
l = [i*i for i in range(20)]
print(l)


# 3)
l = [i**i for i in range(10)]
print(l)


# 4)
l = [i+10 for i in range(11)]
print(l)


# 5)
l = [i-10 for i in range(10)]
print(l)


# 6) with using LC :
l = [i for i in range(1,21) if i % 2 == 0]
print(l)

# 7) without using LC :
l = []
for i in range(1,21):
    if i%2==0:
        l.append(i)
print(l)


# 8)
names = ['priyanka', 'zini', 'jack', 'rahul']
l = [i[0] for i in names]
print(l)

# 9)
names = ['priyanka', 'zini', 'jack', 'rahul']
l = [i[0:4] for i in names]
print(l)


# 10) create a new list by add the element which is containing letter 'a' .

names = ['priyanka', 'rahul', 'jack', 'zini', 'archana']

l = [i for i in names if 'a' in i]
print(l)


# create a new list by using condition in which print 'hello' instead of rahul.

names = ['priyanka', 'rahul', 'jack', 'zini']

l = [i if i!='rahul' else 'hello' for i in names]
print(l)


# create a list from tuple.
t = (11,22,33,44,55,66,77,88,99,100)
l = [i for i in t]
print(l)


# 11)
t = (11, 22, 33, 44, 55, 66)
l = [i for i in t if i % 2 == 0]
print(l)


# create a list from string.
name = "priyanka"
l = [i for i in name]
print(l)

# creation of matrix by using list comprehension.

m = [[j for j in range(3)] for i in range(3)]
print(m)
