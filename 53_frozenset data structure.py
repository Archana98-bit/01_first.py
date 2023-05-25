# 1)
s = {34, 67, 89, 45, 35}
fs = frozenset(s)
print(fs)
print(type(fs))


# create a frozenset from list :
l = [24, 56, 78, 36, 98]
fs = frozenset(s)
print(fs)


# 3)
fs = frozenset(range(11))
print(fs)


# applying other normal method which will not modify frozenset.

fs1 = frozenset([10, 20, 30, 40, 50])
fs2 = frozenset([11, 22 , 33, 44, 50])
fs3 = frozenset([50, 54])
fs5 = frozenset([89,111])

fs4 = fs1.copy()
print(fs4)


print(fs1.union(fs2))

print(fs1.intersection(fs2))

print(fs1.difference(fs2))

print(fs1.symmetric_difference(fs2))

print(fs3.issubset(fs1))

print(fs1.issuperset(fs3))

print(fs5.isdisjoint(fs3))

