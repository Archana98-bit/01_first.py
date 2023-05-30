# 1)
s = 'archana'
d = {}
for i in s :
    d[i] = d.get(i,0)+1   # creating items & updation
print(d)



# 2)
s = 'tushar'
d = {}
for i in s :
    d[i] = d.get(i,0)+1
print(d)



# 3)
s = 'at rs up 123 22'
d = {}
for i in s:
    d[i] = d.get(i,0)+1
print(d)

for i, j in d.items() :
    print(f'{i} is present {j} times')

