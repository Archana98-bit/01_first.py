# 1)
#import random
#rn = random.randint(1,10)

#while True :
    #choice = int(input("Guess a number in between 1 - 10 :"))

    #if choice == rn :
        #print("Congratulations ! you guess correct number")
        #break
    #elif choice > rn :
        #print("Sorry ! your guess number is greater than computer generated number")
    #else :
        #print("Sorry ! your guess number is less than computer generated number")


# 2)
import random
rn = random.randint(1,10)
count = 0

while True :
    count = count-1
    choice = int(input("Guess a number in between 1 - 10 :"))

    if choice == rn :
        print("Congratulations ! you guess correct number")
        break
    elif choice > rn :
        print("Sorry ! your guess number is greater than computer generated number")
    else :
        print("Sorry ! your guess number is less than computer generated number")

print(f'you have taken {count} steps to guess the number ')
