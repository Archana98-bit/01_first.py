for i in range(3):
    for j in range(3):
        print("i={} j={}".format(i,j))

x=[1, 2]
y=[4, 5]
for i in x:
    for j in y:
        print(i,j)

# PRINTING MULTIPLICATION TABLE USING PYTHON.

for i in range(3, 6):
    for j in range(1, 11):
        print(i, "*", j, "=", i*j)
        print()

# PRINTING USING DIFFERENT INNER AND OUTER LOOPS.

list1 = ['I am', 'You are']
list2 = ['healthy', 'fine']
list2_size = len(list2)
for item in list1:
    print("start outer for loop")
    i = 0
    while(i<list2_size):
        print(item, list2[i])
        i = i+1
        print("end for loop")

