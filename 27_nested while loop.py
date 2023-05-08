i=1
while i<=3:
    print('welcome')
    j=1
while j<=3:
    print('to python')
    j=j+1
i=i+1

# other examples.

x=[1,2]
y=[4,5]
while i<len(x):
    j=0
    while j<len(y):
        print(x[i], y[j])
        j=j+1
    i=i+1

# printing multiplication table using nested loop .

for i in range(2,4):
    for j in range(1,11):
        print(i,'*',j,'=',i*j)
        print()