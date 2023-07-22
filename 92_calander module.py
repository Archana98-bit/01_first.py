# Calender module :
# 1)

import calendar as c
days_name = list(c.day_name)
#print(days_name)
#for i in days_name :
    #print(i)

#for i in days_name :
    #print(i[:-3])

da = list(c.day_abbr)
print(da)
for i in da :
    print(i)

# 2)

mn = list(c.month_name)
#print(mn)
for i in mn :
    if i == '':
        continue        # for removing empty space
    print(i)


# 3)
print(c.isleap(2020))

print(c.isleap(2019))


# 4)
print(c.leapdays(2000,2022))

print(c.weekday(2023,7,21))

print(c.weekheader(3))

print(c.calendar(2023))

print(c.monthcalendar(2023,9))

# 5)
print(help(c.day_name))

print(help(c.monthcalendar))

print(dir(c))
