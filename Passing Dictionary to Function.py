l = []
d = {}

def freqcount(list1, dict1):
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] =1
    return dict1

for i in range(int(input('Enter number of elements: '))):
    l.append(int(input('Enter element: ')))

dict1 = freqcount(l, d)
for i in dict1:
    print(f'{i}: {dict1[i]}')