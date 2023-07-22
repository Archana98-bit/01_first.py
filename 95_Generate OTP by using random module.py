# Creation of 4 digit OTP by using manual way.
import random
print(random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9), sep='' )


# Generating 4 digit OTP by using loop.

otp = ''

for i in range(4) :
    otp = otp+str(random.randint(0,9))
print(otp)


# 3)
otp = random.randint(0000,9999)
print(otp)

