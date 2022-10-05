l1 = []

def sum_avg(list):
    sum = 0
    for i in list:
        sum += i
    return sum, sum / len(list)

for i in range(int(input('Enter number of elements in list: '))):
    l1.append(int(input('Enter element: ')))

print(sum_avg(l1))
