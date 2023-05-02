# input a student mark and check the result.
# pass or fail.

mark=int(input('enter your mark'))

if mark>=30:
    print('congratulations!')

if mark<30:
    print('sorry!')

# if-else :

if mark>=30:
    print('congratulations!')

else:
    print('sorry!')


# if-elif-else :

num=int(input('enter the number in between 1-4'))

if num==1:
    print('priyanka')

elif num==2:
    print('rahul')

elif num==3:
    print('zini')

elif num==4:
    print('jack')

else:
    print('invalid option')
