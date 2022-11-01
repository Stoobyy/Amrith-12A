l1 = []

def sum_avg(list):
    sum = 0
    for i in list:
        sum += i
    return sum, sum / len(list)

for i in range(int(input('Enter number of elements in list: '))):
    l1.append(int(input('Enter element: ')))

data = sum_avg(l1)
print(f'Sum of elements in list is {data[0]}\nAverage of elements in list is {data[1]}')
