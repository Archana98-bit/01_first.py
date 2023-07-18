# 1)
def add(a,b) :
    print(a+b)

print(__name__)


# 2)

def add(a,b) :
    print(a+b)

add(100,20)
print(__name__)


# 3)
def add(a,b) :
    print(a+b)

if __name__ == '__main__' :
    add(10,20)
else :
    print('mod1 execute indirectly')
