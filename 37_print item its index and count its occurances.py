# WAP to search a value from a list then display its index if the value is present
# multiple times then print its all indices and also count the number of times
# that value is repeated in the list.

l = [10, 40, 50, 80, 100, 10, 70, 100, 60]
i = 0
count = 0
key = int(input('enter the key to search : '))
while i < len(l):
    if key == l[i]:
        print(f'{key} is present at {i} index ')
        count=count+1
    i = i + 1
print(f'{key} is present {count} times ')
