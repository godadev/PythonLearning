from random import *


def greeting():
    print('*****************************************************************************')
    print('WELCOME TO THE NUMBER GUESSING GAME')
    print('*****************************************************************************')


def game_difficulty():
    diff_number = input('Please enter a number from zero to how much you like. But the higher the number the harder '
                        'the game: ')
    return diff_number


def player_guess():
    number = input('Please guess the number I\'am thinking of right now.')
    return number


random_num = randint(0, int(game_difficulty()))
print(random_num)
guess_num = None

while guess_num != random_num:
    try:
        guess_number = int(player_guess())
        if guess_number > random_num:
            print('I am thinking of a lower number!')
        if guess_number < random_num:
            print('I am thinking of a higher number!')
        if guess_number == random_num:
            print('YOU WON!!!')
            break
    except ValueError:
        print('We need an integer.')
        continue
