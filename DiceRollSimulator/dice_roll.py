import random

print('Welcome to the Dice Rolling simulator.')


def change_type():
    print('Select the type of dice you would like to roll: \n A. 6-sided, \n B. 8-sided, \n C. 20-sided')
    response = input('Type A, B, or C: ')
    if response.upper() == 'A':
        return 6
    elif response.upper() == 'B':
        return 8
    elif response.upper() == 'C':
        return 20
    else:
        print('Input is invalid. Exiting program . . .')
        exit()


def change_num():
    print('How many dice would you like to roll?')
    response = int(input('Type a number between 1 and 5, inclusive: '))
    return response


def replay():
    return str(input('Would you like to play again? Type Y or N: '))


play_again = 'Y'
smallest = 1
largest = change_type()
num = change_num()
sides = num

while play_again == 'Y':
    if sides == 1:
        plural = 'dice'
    else:
        plural = 'die'
    print('rolling {} {}-sided {} . . .'.format(num, largest, plural))
    while num != 0:
        print(random.randint(smallest, largest))
        num -= 1
    if num == 0:
        play_again = replay()
        if play_again == 'Y':
            type_replay = input('Would you like to change the type of dice? Type Y or N: ')
            if type_replay == 'Y':
                largest = change_type()
            num_replay = input('Would you like to change the number of dice to roll? Type Y or N: ')
            if num_replay == 'Y':
                num = change_num()
            else:
                num = sides

print('\n Thanks for playing. Goodbye!')
