# Print list in reverse order using positive index.

l = [11, 22, 33, 44, 55, 66, 77, 88, 99]
a = len(l)-1
while a >= 0:
    print(l[a])
    a = a-1


# Print list in reverse order using negative index.

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = -1
while i >= -len(l):
    print(l[i])
    i = i-1

# Find the minimum value from a list.
l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
min = l[0]

for i in l:
    if i < min:
        min = i

print("min value is : ",min)

# Find the maximum value from a list.
l = [1,9,6,8,5,10,53,89,64,57]
max = l[0]

for i in l:
    if i > max:
        max = i
print("max value is :",max)

