# 1)

import hellocal        # here we are importing hellocal modules that means we can access
# all the members of hellocal modules
print(hellocal.add(10,20))
print(hellocal.sub(100,20))
print(hellocal.pi)


# 2)

import math
print(math.factorial(3))
print(math.factorial(5))



# 3) module aliashing :

import hellocal as h
print(h.add(100,10))
print(h.mul(4,5))
print(h.pi)
print(hellocal.sub(70,67))


# 4) Different ways of importing modules :

from hellocal import add, sub, mul, div
print(add(70,45))
print(sub(100, 20))
print(mul(56,5))
print(div(56,7))


# or,
from hellocal import *
print(mul(6,8))
print(pi)


# Module member aliash :

from hellocal import add as a, sub as s, pi as p, mul as m
print(a(5,10))
print(m(6,3))
print(p)
