# Direct execution :
print(__name__)


# 2)

import mod1
print(__name__)

# 3)

import mod1
mod1.add(100,200)
print(__name__)

