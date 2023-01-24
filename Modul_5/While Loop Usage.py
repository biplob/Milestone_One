student = []

while True:
    name = input('Enter Students Name: ')
    if name == 'shesh':
        print(student)
        print('Total Students: ', len(student))
    else:
        student.append(name)
