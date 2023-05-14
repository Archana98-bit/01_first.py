# Concatenate of list.
l = [23, 33, 43, 53, 63, 73]
s = ['priyanka','zini','jack', 45, 67, 78]
a = [6.89, 98.7, True, False]
r = l+s+a
print(r)

# Repeatation of list.
l = [11, 22, 33, 44, 55]
r = l*3
print(r)

# Membership operator ('in' operator and 'not in' operator).
l = [10, 11, 12, 13, 14, 15, 16, 17]
print(13 in l)
print(15 not in l)
print(78 in l)
print(89 not in l)

# WAP to check whether your lucky number is present inside a list or not.
l = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
choice = int(input("Enter your lucky number : "))
if choice in l:
    print("Yes! Your lucky number is present in the list")
else:
    print("Sorry! Your lucky number isn't present in the list")


# WAP to check your lucky number until match your lucky number with list element.
l = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
choice = int(input("Enter your lucky number : "))
while True:
    if choice in l:
        print(" Yes! Your lucky number is present inside the list ")
        break
    else:
        print(" Sorry! Your lucky number isn't present inside the list ")
        choice = (int(input("Enter your lucky number again : ")))
