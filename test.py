a = list(eval(input('Enter tuple: ')))
large = a[0]
small = a[0]

while True:
    inp = int(input('1) Accept an element to add to the tuple.\n2) Display the largest and smallest of the tuple.\n3) Update all even numbers by adding 2 and odd numbers by adding 3.\n4) Perform a linear search of an element in a tuple.\n5. Exit\nEnter number corresponding to the option:'))

    if inp == 1:
        a += [int(input('Enter number to add to tuple: '))]
        print(f'The tuple is now {tuple(a)}')

    elif inp == 2:
        for i in a:
            if i > large:
                large = i
            elif i < small:
                small = i

        print(f'Small = {small}\nLarge = {large}')

    elif inp == 3:
        for i in range(len(a)):
            a[i] += 2 if a[i]%2 == 0 else 3

        print(f'The tuple is now {tuple(a)}')

    elif inp == 4:
        pos = 0
        element = int(input('Enter element to search for: '))
        if element in a:
            for i in range(len(a)):
                if a[i] == element:
                    pos = i
            print(f'Element is at position {pos}')
        else:
            print('Element not found.')
    
    elif inp == 5:
        break

    else:
        print('Invalid Option.')
