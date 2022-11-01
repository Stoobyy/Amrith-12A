org_dict = {'roll': 1, 'name': 'Ram', 'percentage': 95}

def updatedictionary(passed_dict, key, value):
    passed_dict[key] = value
    return passed_dict

while True:
    print('Current Dictionary', org_dict)
    opt = int(input('1. Change roll no.\n2. Change name\n3. Change percentage\n4. Exit\nSelect an option: '))

    if opt == 1:
        roll = int(input('Enter new roll number: '))
        a = updatedictionary(org_dict, 'roll', roll)
    elif opt == 2:
        name = input('Enter new name: ')
        a = updatedictionary(org_dict, 'name', name)
    elif opt == 3:
        percentage = int(input('Enter new percentage: '))
        a = updatedictionary(org_dict, 'percentage', percentage)
    elif opt == 4:
        break



