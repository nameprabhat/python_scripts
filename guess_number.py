##guess the number game

import random , sys

print ('hello! whats your name')
name = input()

print ('lets play a guess game '+ name + ' i will give you 6 chances for guessing')

##sys.exit()
guess = random.randint(1,20)

print ('DEBUG:secret number is '+ str(guess))

try:
    for i in range (1,7):
        print ('Guess a number')
        num = int(input())
        if num == guess:
            print ('you guessed it correctly..congrats and you took ' +str(i) + ' attempts'  )
            break
        elif num < guess:
            print ('guess again your values is low')
        elif num > guess:
            print ('guess again your values is high')
        else:
            print ('your turn is over, correct number is '+ str(guess))

    if num != guess:
        print ('your turn is over, you have taken ' + str(i) +' attempts without success correct number is '+ str(guess))

except:
    print ('enter number only')
