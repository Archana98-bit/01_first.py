# Delete statement :
# 1)
a=50000
print(a)
del a
print(a)

# 2)
name="archana"
print(name)
del name
print(name) # not possible

# 3)
l=[10, 20, 30, 40, 50]
print(l)
del l
print(l) # not possible because variable(l) already deleted

# 4)
l=[10, 20, 30, 40, 50]
print(l)
del l[4]
print(l)

# None statement - variable name isn't deleted and it is already present inside a memory :
# 1)

name="archana"
print(name)
name = None
print(name)
name="Tushar"
print(name)