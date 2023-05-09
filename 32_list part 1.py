# 1)
l=[10,20,30,40,'priyanka','rahul','zini','jack',8.90,56.7]
print(l)

# 2)
l=[10,20,30,'archana','priyanka',40.89]
print(l[-2])
print(l[3])

# 3) CREATION OF EMPTY LIST :
l=[]
print(l)

# 4) CREATION OF LIST USING DYNAMICALLY USING eval() FUNCTION :
l = eval(input("enter a list : "))
print(l)

# 5) CREATION OF LIST USING list() FUNCTION :
l = list((11,22,33,44,55))
print(l)

# 6) CREATION OF LIST USING range() FUNCTION :
l = list(range(10,20))
print(l)

# 7) CREATION OF LIST DIRECTLY :
# List can hold any complex data type like dict, tuple, etc.
# a)
l = [11, 22, 'archana', True, 67.9]
print(l)

# b)
l = [11, 22, {"name": "archana"}, list((10,20,44))]
print(l)

# 8) split() Function :
msg = "welcome to python class"
l = msg.split()
print(l)

# Accessing elements of list using index :
l = [11,22,33,44,55,66]
print(l[0])
print(l[1])
print([-1])
print([-2])
print(l[20])

# Accessing elements of list using slice operator :
l = [23, 34, 45, 56, 78]
print(l[::])
print(l[2::2]) 