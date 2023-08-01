# Generate fake students data :
# a) Generate students data :

from random import *
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(10) :
    fname = choice(alpha).upper()
    lname = choice(alpha).upper()
    for i in range(3,13) :
        fname = fname+choice(alpha)
        lname = lname+choice(alpha)
    print(fname,lname)


# b) student mobile no. :
digits = "0123456789"

for i in range(10) :
    smob = choice('9876')

    for i in range(9) :
        smob = smob+choice(digits)
    print(smob)



# student age :
for i in range(10) :
    sage = randint(16, 25)
    print(sage)


# student address :
cities = ['BBSR', 'CTC', 'ANU', 'BLS', 'JAJ', 'KDP', 'KAL', 'NAY', 'ROU', 'SUN']

for i in range(10) :
    saddr = choice(cities)
    print(saddr)


# student branch :
course = ['BTech.', 'BCA', 'MCA', 'MBA', 'BBA', 'MTech.']

for i in range(10) :
    scourse = choice(course)
    print(scourse)



# student ID :
digits = "0123456789"

for i in range(10) :
    sid = 'ABC-'
    for i in range(6) :
        sid = sid+choice(digits)
    print(sid)


# student DOB :
def generate_sdob() :
    day = random.randint(1, 30)
    month = random.randint(1,12)
    year = random.randint(1990, 2001)
    return day, month, year
students_dob = []

for i in range(10) :
    dob = generate_sdob()
    students_dob.append(dob)

for i, dob in enumerate(students_dob, 1) :
    day, month, year = dob
    print(f'student {i}: {day}-{month}-{year}')


