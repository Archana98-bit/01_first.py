# Visiting all the elements in a sequence is called Traversing.

# Traversing list using for loop :
l = [10, 20, 30, 40, 50]
for i in l:
    print(i)

# Traversing list using while loop :
# 1)
l = [11, 22, 33, 44, 55]
i = 0
while i < len(l) :
    print(l[i])
    i = i + 1

# 2)
l = [10, 20, 30, 8, 67, 40, 50, 60]
for i in l :
    if i % 4 == 0 and i % 8 == 0 :
        print(i)

# Iterate over list :
l = [10, 20, 30, 40, 50]
length = len(l)
for i in range(length):
    print(l[i])

# Traversing list using enumerate():
l = [10, 20, 30, 40, 50]
for i, val in enumerate(l):
    print(i, ",", val)

# Traversing list using iter function and the next function :
list = [10, 30, 50, 70, 90]
iterator = (list)
try:
   while True:
    element = next(iterator)
    print(element)
except StopIteration :
    pass

# Traversing list using map() function :
def print_element(element):
    print(element)
my_list = [10, 20, 30, 40, 50]
result = map(print_element, my_list)
for _ in result:
    pass

# WAP to display list elements of a list along with positive and negative index.
l = [11, 22, 33, 44, 55, 66] 
n = len(l) 
for i in range(n):
    print(l[i], i, i-n)
