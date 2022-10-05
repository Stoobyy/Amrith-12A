tup = ()

def odd_even(tup):
    odd= 0
    even = 0
    for i in tup:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd,even

for i in range(int(input('Enter number of elements:' ))):
    tup += (int(input('Enter element: ')), )

result = odd_even(tup)
print(f'Odd: {result[0]}\nEven: {result[1]}')


