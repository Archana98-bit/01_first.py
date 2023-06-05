# 1) list merging :
l = [101, 102, 103, 104, 105]
s = [100, 200, 'priyanka']
p = l+s
print(p)


# 2) tuple merging :
t = (100, 200, 300, 400, 500)
s = (101, 105, 'rahul')
m = t+s
print(m)


# 3) set merging :
s1 = {1000, 2000, 3000, 4000}
s2 = {1001, 'zini', 1002}
s3 = {*s1, *s2}
print(s3)


# 4)
d1 = {1:'priyanka', 2:'rahul'}
d2 = {3:'zini', 4:'jack'}
d3 = {*d1, *d2}
print(d3)
d4 = {**d1, **d2}
print(d4)

