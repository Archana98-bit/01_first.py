# Creation of Set.
# Creation of empty set by using set() function.

s = set()
print(s)
print(type(s))


# Creation of set with multiple elements.
# 1)
s = {45, 67, 90, 67, 56}
print(s)
print(type(s))


# 2)
s = {34, 78, 89, 'priyanka', 'rahul', 78.9, True, False}
print(s)
print(type(s))


# Creation of set with set() function from list.

l = [34, 87, 90, 56, 43, 'priyanka', 98.6, True]
s = set(l)
print(s)
print(type(s))


# Creation of set from tuple.

t = (89, 45, 43, 25, 'priyanka', 67.9, True)
s = set(t)
print(s)
print(type(s))



# Creation of set from range().

s = set(range(21))
print(s)
print(type(s))


# Creation of set from string.
# 1)
name = "Archana pati"
s = set(name)
print(s)
print(type(s))

# 2)
name = "Archana pati"
s = set(name.split())
print(s)
print(type(s))

# 3)
s = set("Archana pati")
print(s)
print(type(s))


