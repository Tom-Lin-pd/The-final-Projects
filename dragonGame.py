import random
import time
#This happens to be a mini dragon game. 


def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print(' and will share your treasure with you. The other Dragon')
    print('is greedy and hungry, and will eat you in sight.')
    print('People say that they sometimes change their caves, so be careful.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chooseCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky... (are you brave enough?)...')
    time.sleep(2)
    print('A big and fat dragon jumps out of the cave in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chooseCave == str(friendlyCave):
        print('Gives you his treasure!')
        print('')
        time.sleep(1)
        print('Nice, but now start to run, the other dragon is coming to eat you up!!')
    else:
        print('Gobbles you down in one bite')
        time.sleep(1)
        print('NICE')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()

    
