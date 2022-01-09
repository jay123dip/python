import random
number = random.randint(1, 50)
# print("number is "+str(number))
for i in range(0,3):
    user=int(input('guess the number :'))
    if user==number:
        print("You Win !!!")
        break
    if user!=number:
        print("You Lose !!!")
        if(user>number):
            print('you guess is greater than the number')
        else:
            print('you guess is less than the random number')
        
