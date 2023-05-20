# add() method :
# 1)
s = {34, 76, 89, 64, 47}
s.add(980)
print(s)


# 2)
s = {45, 78, 86, 86}
s.add('priyanka')
print(s)


# 3)
s = {645, 908, 876, 643}
s.add(897.67)
print(s)


# 4)
s = {78, 90, 65, 37, 73}
s.add(True)
print(s)


# 5)
s = {67, 90, 54, 73, 42}
s.add(90)
print(s)


# update() method :
# 1)
s = {45, 89, 76, 54, 32, 41}
l = [3, 6, 8, 9, 4, 2]
t = (10, 20, 30, 40, 50)

s.update(l, t)
print(s)


# 2)
s = {87, 90, 75, 38, 28}
l = ['priyanka', 86, 98, 143]
t = (76, 69, 37, 'rahul', 96)

s.update(l, t, range(89, 97))
print(s)


# 3)
s = {76, 98, 90, 53, 23}
s.update([654, 890])
print(s)


# 4)
s = {89, 64, 36, 86, 92}
s.update(range(67, 89), range(68, 90, 38))
print(s)


# remove() method :
# 1)
s = {87, 90, 56, 48, 28}
s.remove(56)
print(s)

# 2)
s = {67, 89, 35, 27, 25}
s.remove(68)      #KeyError : 68
print(s)


# discard() method :
# 1)
s = {45, 78, 90, 59, 38}
s.discard(78)
print(s)


# 2)
s = {56, 89, 39, 20, 49}
s.remove(567)
print(s)


# pop() method :
s = {54, 78, 39, 28, 49}
s.pop()
print(s)
print(s.pop())



# copy() method :
s1 = {45, 89, 38, 20, 50}
s2 = s1.copy()
print(s1)
print(s2)


# clear() method :
s = {34, 78, 49, 39, 29, 90}
print(s)
s.clear()
print(s)


# enumerate() method :
# 1)
s = {54, 67, 39, 29, 59, 21}
for i in enumerate(s) :
    print(i)


# 2)
s = {35, 78, 40, 39, 28}
for i, j in enumerate(s) :
    print(i, ' ', j)



# min() and max() method :
s = {76, 49, 39, 27, 63, 35}
print(min(s))
print(max(s))


# sum() method :
s = {98, 48, 39, 24, 50, 73}
print(sum(s))


# sorted() method :
s = {47, 78, 39, 29, 50, 21}
print(sorted(s))
print(sorted(s, reverse=True))
