import random
import time

def magic_ball():
    response = ['you cant be serious','well i guess there is solution to your problem','i cant tell','yeah could be','not so sure','you are right','certainly not',
                'the gues it right','yeah i still love her','i dont care','yes, of couse am with you']
    while True:
        question = str(input('Ask your mysterious question:\n'))
        for i in range(0,4):
            print('shaking the ball..')
            time.sleep(0.30)
        print(response[random.randint(0,len(response)-1)])
        
    
magic_ball()
