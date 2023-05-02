# WAP input three numbers and check which one is greatest using if-elif-else condition.

a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
c=int(input('enter the value of c'))

if a>b and a>c:
    print('a is greater')

elif b>c:
    print('b is greater')

else:
    print('c is greater')