a = input('Enter String: ')

opt = int(input('1) Print the count of letters in the string\n2) Print the number of upper-case, lower-case, vovels and digits\n3) Reverse the string and check whether its a palindrome\nEnter an option corresponding to you choice: '))

if opt == 1:
    leng = {}
    for i in a:
        if i in leng:
            leng[i] += 1
        else:
            leng[i]= 1
    print(leng)

elif opt == 2:
    upper = 0
    lower = 0
    vovel= 0
    digit = 0
    digitlist = ['1','2','3','4','5','6','7','8','9','0']
    vovellist = ['a','e','i','o','u','A','E','I','O','U']

    for i in a:
        if 'A' <= i <= 'Z':
            upper += 1
        elif 'a' <= i <= 'z':
            lower += 1
        if i in digitlist:
            digit += 1
        if i in vovellist:
            vovel += 1
    
    print(f'Upper: {upper}\nLower: {lower}\nDigits: {digit}\nVovels: {vovel}')

elif opt == 3:
    if a == a[::-1]:
        print('It is a palindrome')
    else:
        print('Not a palindrome')

else:
    print('Invalid Option')