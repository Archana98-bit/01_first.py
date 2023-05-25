# 1)
myinfo = {
       'name': 'Archana pati',
       'email': 'archana@gmail.com',
       'addr' : 'Bhubaneswar',
       'mob' : 9098753567
}

print(myinfo)
print(myinfo['mob'])
print(type(myinfo))


# 2) Different ways for creating dict.
# empty dict :

d = {}
print(d)
print(type(d))


# Creating an empty dict then add item.
d = {}
d['name'] = 'Archana'
d['mob'] = 9874620915
d['addr'] = 'BBSR'

print(d)


# Create dict directly.

roll = {1:'priyanka', 2:'rahul', 3:'zini', 4:'jack'}
print(roll)
print(type(roll))


# Check the key is exists or not.
# has_key() :

roll = {1:'priya', 2:'swapna', 3:'sahil', 4:'sunil'}
print(roll.has_key(3))


# Solutions for this :

roll = {1:'priya', 2:'swapna', 3:'sahil', 4:'sunil'}
print(2 in roll)     # use in operator


# Create a dictionary dynamically by taking user input.

d = {}

while True:
    key=input('Enter the key')
    val=input('Enter the value')
    d[key]=val

    choice=input('Do you want to add more element [Y/N]')

    if choice == 'N':
        break

print(d)


# Traversing a dict :

roll = {1:'priyanka', 2:'rahul', 3:'zini', 4:'jack'}

for i in roll:
    print(i)


# print key and value.

roll = {1:'sahil', 2:'rupesh', 3:'sushil'}
for i in roll:
    print(i, roll[i])


# Add, modify, delete dictionary items.
# Add item :

d = {1:'sahil', 2:'supriya', 3:'sushil', 4:'sujata'}
print(d)
d['5'] = 'suresh'
print(d)


# Modify item :

d = {22:'rakesh', 23:'soumya', 24:'neha', 25:'dipu'}
print(d)
d[25] = 'rupali'
print(d)

d[990] = 'welcome'
print(d)


# Delete item :

d = {11:'suku', 22:'puku', 33:'ruku', 44:'chuku'}
print(d)
del d[22]
print(d)


# Delete all the items.

d = {10:'susmita', 20:'rashmi', 30:'dethi', 40:'rekha'}
print(d)
d.clear()
print(d)


# how to delete entire dictionary.

d = {10:'smruti', 20:'rupali', 30:'rekha', 40:'rahul'}
print(d)
del d
print(d)


