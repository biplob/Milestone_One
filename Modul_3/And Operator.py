number = int(input('Enter the number: '))

if number >= 80 and number <= 100:
    print('A+')
elif number >= 70 and number <= 79:
    print('A')
elif number < 60 and number >= 0:
    print('You are failed')
else:
    print('Invalid Number')