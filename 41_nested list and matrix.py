# Nested lists.
# 1)
l = [11,22,33,[44,45,46,47],55,66,77,88,]
print(l)
print(l[3])
print(l[3][2])
print(l[3][-3])
print(l[-5][-2])

# 2)
l = [10, 20, 30, 40, 50, [60,61,62,63], 70, [80,81,82,83,85], 90, 100]
print(l)
print(l[7])
print(l[7][-3])
print(l[5][3])
print(l[-3][-2])
print(l[2:3])
print(l[5:4])
print(l[-3:-2:1])


# 3)
l = [10, 20, 30, [40,41,42,43,44,[1,2,3,4,5],45], 50, 60]
print(l[-3])
print(l[-3][-1][-2])
print(l[3][0])


# 4) Nested matrix in row wise print using loop concept.
l = [
       [11, 22, 33]
       [44, 55, 66]
       [77, 88, 99]
]

for i in l:
    for j in i:
        print(j, end=' ')
    print(' ')
    