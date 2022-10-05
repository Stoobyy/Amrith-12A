def str_update(string):
    newstring = ''

    for i in string:
        if i.isupper():
            newstring += i.lower()
        elif i.islower():
            newstring += i.upper()
        elif i.isdigit():
            newstring += '@'
        elif i == ' ':
            newstring += '*'

    return newstring

string = input('Enter string: ')
print(f'Updated string: {str_update(string)}')