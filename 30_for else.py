# for else statement :
# if for loop execute fully without break then else loop will execute.
# if break executed inside for loop then else block won't be execute.

# 1)
for i in range(10):
    print(i)
else:
    print("else block")

# 2)
for i in range(1, 4):
    print(i)
else:
    print("No break")

# 3) WAP to check if an array constants of even number.

def contains_even_number(l):
    for ele in 1:
        if ele % 2 == 0:
            print("list contains an even number")
            break
    else:
        print("list doesn't contain an even number")
print("for list 1:")
contains_even_number([1, 9, 8])
print("\nfor list 2:")
contains_even_number([1, 3, 5])