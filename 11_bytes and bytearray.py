# List to bytes.
a=[10,20,30,40,50]
b=bytes(a)
print(b[3])
print(b[-4])

for i in b:
    print(i)

    #convert list to bytearray.
    a=[10,20,30,40,50,60,70,80,90,100]
    b=bytearray(a)
    print(b[-3])
    print(b[2])

    for i in b:
        print(i)

# modify index value.
b[2]=230
for i in b:
    print(i)
