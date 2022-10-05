a = []
odd = 0
even = 0
oddsum = 0
evensum = 0
freq = {}

for i in range(int(input('Enter number of elements:'))):
    b=int(input('Enter number: '))
    a+=[b]
    if b%2 == 0:
        even += 1
        evensum += b
    else:
        odd += 1
        oddsum += b

for i in a:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] = freq[i]+1

        
opt = int(input('What do you want to do?\n1.Print the count and sum of all odd numbers\n2.Print and count the sum of all even numbers\n3.Count the frequency of an element from the list\n4.Remove duplicates from the dictionary\n5.Rotate the list\nChoose an option: '))

if opt == 1:
    print(f'The sum is {oddsum} and there are like {odd} odd elements in the list.')

elif opt == 2:
    print(f'The sum is {evensum} and there are like {even} odd elements in the list.')

elif opt == 3:
    element1=int(input('Enter element to search for:'))
    print(f'Frequency is {freq[element1]}.')

elif opt == 4:
    a2=[]
    for i in a:
        if i not in a2:
            a2 += [i]
    a = a2
    print(f'The list is now {a}.')

elif opt == 5:
    a = a[-1:] + a[0:-1]
    print(f'The list is {a}.')

else:
    print('Invalid selection. Please rerun the program.')
