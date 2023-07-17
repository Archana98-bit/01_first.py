# Naming conflict while importing member from two different module(data and cal)

# 1)

import cal
import data
print(cal.a)
print(data.a)


# 2)

from cal import a
from data import a
print(a)


# 3)

from data import a
from cal import a
print(a)


# 4)

from cal import *
from data import *
print(a)



# 5)

from cal import a as x
from data import a as y
print(x)
print(y)

