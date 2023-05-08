# Print multiplication table of a number.i. 

num=int(input('enter a number of which the user wants to print the multiplication table:'))
print('the multiplication table of:', num)
for i in range(1,11):
    print(num,'*',i,'=',num*i)

# Print each fruit in a fruit list.

fruits=["apple","banana","cherry","pineapple","litchy","orange"]
for x in fruits:
    print(x)
    if x == "cherry":
        break