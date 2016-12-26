#!usr/bin/env python
"""
numberGuess.py
Guess the number
"""

import random

def main():
    number = random.randint(1, 20)
    print('NUMBER GUESS')
    loop = True
    while loop == True:
        answer = int(input('guess a number between 1-20: '))
        if answer > number:
            print('Too high')
        elif answer < number:
            print('Too low')
        elif answer == number:
            print('You are right!, the answer is %s' % (number))
            loop = False
        else:
            print('please guess a number between 1-20')

    playAgain = input('Do you want to play again? (y/n)')
    if playAgain == 'y':
        main()
    else:
        exit()

if __name__ == '__main__':
    main()

print