# break statement :

# 1)
for i in range(2, 4):
 for j in range(1, 11):
  if i == j:
   break
print(i, "*", j, "=", i*j)
print()

# 2)
for i in range(10):
 if i == 7:
  break
print(i)

# 3)
list1 = [[j for i in range(3)]
         for i in range(5)]
print(list1)

# continue - skip statement :
# 1)
for i in range(3, 6):
 for j in range(1, 11):
  if i == j:
   continue
print(i, "*", j, "=", i*j)
print()

# 2)
for i in range(10):
 if i == 5 or i == 8:
        continue
 print(i)

# 3)
for i in range(10):
  if i == 5:
    continue
print(i)

# pass - empty statement :
# if you want to provide empty body then go for pass statement.
# Do nothing.

# 1)
for i in range(10):
  if i%2 == 0:
    print(i)
  else:
    pass

# 2)
for i in range(10):
  if i%2 == 0:
    pass
else:
  print(i)