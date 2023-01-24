marks = int(input('Enter your marks: '))
weight = int(input('Enter your weight: '))

# if marks >= 80 or weight <=20:
#     print('You will get a chocklet')
# else:
#     print(' You get less amount of marks and over weight')

if not (marks <= 79 or weight >=20):
    print('You will get a chocklet')
else:
    print(' You get less amount of marks and over weight')