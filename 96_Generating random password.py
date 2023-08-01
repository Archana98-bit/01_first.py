# 1) Create 8 char password that must contain alphabets, digits and some special symbols.
import random
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
special_symbols = '!@#$%^&*()_+-{}><~/'
print(random.choice(alpha),random.choice(digits),random.choice(special_symbols),random.choice(alpha),random.choice(digits),random.choice(special_symbols),random.choice(alpha),random.choice(digits),sep="")


# 2)
import random
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
special_symbols = '!@#$%^&*()_+-{}><~/'
print(random.choice(alpha),random.choice(digits+special_symbols),random.choice(special_symbols+alpha),random.choice(alpha),random.choice(digits),random.choice(special_symbols),random.choice(alpha),random.choice(digits),sep="")


# 3)
import random
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
special_symbols = '!@#$%^&*()_+-{}><~/'
for i in range(10) :
    print(random.choice(alpha),random.choice(digits),random.choice(special_symbols),random.choice(alpha),random.choice(digits),random.choice(special_symbols),random.choice(alpha),random.choice(digits),sep="")

