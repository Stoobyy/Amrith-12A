d = {}

while True:
    name = input('Enter student name: ')
    d[int(input('Enter Admission Number: '))] = [int(input('Enter roll number: ')), name, int(input('Enter marks: '))]
    y = input('Do you want to continue? (y/n) ')
    if y == 'n':
        break

print(f'Inputted dictionary: {d}')

while True:
    tosearch=int(input('Enter admission number to search for: '))
    if tosearch in d:
        l=d[tosearch]
        print(f'Student name: {l[1]}\nStudent Roll number: {l[0]}\nStudent Adm Number: {tosearch}\nMarks Obtained: {l[2]}')
        y = input('Do you want to continue? (y/n) ')
        if y == 'n':
            break
    else:
        print('Admission number not in dictionary.')