# create a set from list[] :
# without set comprehension :
l = [10, 20, 30, 40, 50]
s = set()

for i in l:
    s.add(i)

print(s)


# with set comprehension :
l = [11, 22, 33, 44, 55]

s = {i for i in l}
print(s)

# 2)
l = [34, 78, 56, 35, 89]

s = {i*2 for i in l}
print(s)


# create a set from rang :
# 1)
s = {i for i in range(20,31)}
print(s)


# 2)
s = {i**2 for i in range(21)}
print(s)


# create a set by adding all the element from 10 to 40 which is divisible by 3.

s = {i for i in range(10, 41) if i % 3 == 0}
print(s)


# create a set from a list called names by adding the first char of each element.
# 1)
names = ['priyanka', 'zini', 'jack', 'rahul']
s = {i[0] for i in names}
print(s)


# 2)
names = ['priyanka', 'zini', 'jack', 'rahul']
s = {i[0].upper() for i in names}
print(s)


# create a set from a list(names) by adding all the elements but if the element is 
# priyanka then instead of priyanka add anjali.

names = ['priyanka', 'zini', 'jack', 'rahul']
s = {i if i != 'priyanka' else 'anjali' for i in names}
print(s)
