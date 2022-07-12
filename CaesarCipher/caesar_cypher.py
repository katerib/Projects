import string

upper, lower = string.ascii_uppercase, string.ascii_lowercase
caesar = 3


def encrypt(shift):

    result = ''

    text = str(input('Type the string to encrypt: '))
    print('This algorithm is using a shift pattern of {}.'.format(shift))
    response = str(input('Would you like to change the shift pattern? Type Y or N: '))
    if response.upper() == 'Y':
        shift = int(input('What would you like to change the shift pattern to? Type an integer value: '))

    for index in range(len(text)):
        if text[index] in lower:
            result += lower[(lower.index(text[index]) + shift) % 26]
        elif text[index] in upper:
            result += upper[(upper.index(text[index]) + shift) % 26]
        elif text[index].isnumeric():
            result += str(int(text[index]) + shift)
        else:
            result += text[index]

    print('\n')
    print('Original string: ', text)
    print('Shift pattern: ', shift)
    encrypted = '| Encrypted string: ' + result + ' |'
    line = ''
    for sym in encrypted:
        line += '-'
    print(line)
    print(encrypted)
    print(line)
    restart(shift)


def restart(shift):
    response = str(input('Would you like to restart? Type Y or N: '))
    if response.upper() == 'Y':
        encrypt(shift)
    else:
        exit()


encrypt(caesar)
