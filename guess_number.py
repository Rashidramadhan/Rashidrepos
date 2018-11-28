import random

guessnumber = random.randint(1,20)
print('am thinking of a number between 1 and 20\n')
for number in range(1,7):
        print('Take a guess')
        guess = int(input())
        if guess < guessnumber:
            print('input is too low')
        elif guess > guessnumber:
            print('input is too high')
        else:
            break
if guess == guessnumber:
        print('Good guess, you got the number in ' + guessnumber+ 'guesses')
else:
        print('nop, the number in mind is ' + str(guessnumber))
            
            

    
