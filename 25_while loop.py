# Print your name 100 times.

i=1
while i<=10:
    print('Archana')
    i=i+1

# Print the number 1 to 10.

i=1
while i<=10:
    print(i)
    i=i+1

# Print the number 90 to 100.

i=90
while i<=100:
    print(i)
    i=i+1

# Print the number 10 to 1.

i=10
while i>=1:
    print(i)
    i=i-1

# Print the number 999 to 990.

i=999
while i>=990:
    print(i)
    i=i-1

# Print the number series like 111 222 333 444 555 666....

i=111
while i<=666:
    print(i)
    i=i+111

# Print the number series like 999 777 555 333...

i=999
while i>=333:
    print(i)
    i=i-222

# Print i as long as i is less than 6.

i=1
while i<6:
    print(i)
    i += 1

# Exit the loop when i is 3.

i=1
while i<6:
    print(i)
    if i==3:
        break
    i += 1

# Continue to the next iteration if i is 3.

i=0
while i<6:
    i += 1
    if i == 3:
        continue 
    print(i)

# Print a message once the condition is false.

i=1
while i<6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')

# Program to calculate the sum of numbers (1) Until the user enters zero
# (2) add the numbers until number is zero

total=0
num = int(input('enter a number:'))
while num != 0:
    total += num
    num = int(input('enter a number:'))
    print('total is =', total)

# To check whether you can vote or not.

age=52
while age>18:
    print('You can vote')
else:
    print('Sorry! You can not vote')

# Print * 10 times.

i=1
while i<=10:
    print('*')
    i=i+1

# OR
i=1
while i<=10:
    print('*',end=' ')
    i=i+1

# Find out sum of n natural numbers.

i=1
while i<=10:
    result =+ i
    i=i+1
    print(result)

# Find out sum of numbers from m to n.

m = 7
n = 11
sum = 0
while m<=n:
    sum =+ m
    m = m + 1
    print(sum)