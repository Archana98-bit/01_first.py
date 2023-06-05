# 1)
d = {1:{'name':'priyanka'}, 2:{'name':'rahul'}, 3:{'name':'zini'}, 4:{'name':'jack'}}

for i in d :
    print(i)


for i in d.values() :
    print(i)


for i,j in d.items() :
    print(i,j)


print(d[1])

print(d[3]['name'])


# 2)
d = {1:{'name':'Rahul'}, 2:{'name':'Zini'}, 3:{5:{6:{7:{8:9}}}}}

print(d[3])
print(d[3][5])
print(d[3][5][6])
print(d[3][5][6][7])


# 3)
d = {1:{'name':'Rahul'}, 2:{'name':'Zini'}, 3:{5:{6:{7:{8:9}}}}}

d[3][5][6][7] = 900

print(d[3][5][6][7])

print(d)


# How to iterate nested dictionary..

students = {10:{'Name':'Priyanka', 'Email':'priyanka@gmail.com', 'Addr':'BBSR'},
            11:{'Name':'Rahul', 'Email':'rahul@gmail.com', 'Addr':'CTC'},
            12:{'Name':'Zini', 'Email':'zini@gmail.com', 'Addr':'Hyd'},
            13:{'Name':'Jack', 'Email':'jack@gmail.com', 'Addr':'Del'}
            }

for k,v in students.items() :
    print('student id is : ',k)

    for i in v:
        print(f'{i} is : {v[i]}')
    print('-'*20)
    