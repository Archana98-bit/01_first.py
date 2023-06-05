# 1)
d = {i:i for i in range(1,11)}
print(d)
print(type(d))

# 2)
d = {i:i*i for i in range(1,11)}
print(d)


# 3) working with list to create dict.

l = [3.2, 6.5, 3.4, 4.7, 5.5]
d = {i:3.14*i*i for i in l}
print(d)


# 4)
names = ['priyanka', 'zini', 'jack', 'rahul']
d = {i:len(i) for i in names}
print(d)


# 5) some conditions apply.
names = ['priyanka', 'rahul', 'zini', 'jack']
d = {i:len(i) for i in names if len(i)>5}
print(d)
