# normal_body_temp = 98.5
# temp = float(input('Enter the tempeture: '))
#
# if temp > normal_body_temp:
#     print("Please eat two bela peracitemal")
# else:
#     print('Just east vitamin C table. ')

# Jalanta is an actor of Bangladesh. He is Nayok
# Rain is an actress of Bangladesh. She is Nayika

name = input('Enter  name: ')
country = input('Enter country name: ')
gender = input('Enter gender: ')

# profession, pronoun, known_as

if gender == 'm':
    profession = 'Actor'
    pronoun = 'He'
    known_as = 'Nayok'

else:
    profession = 'Actress'
    pronoun = 'She'
    known_as = 'Nayika'

print(f'{name} is an {profession} of {country}. {pronoun} is {known_as}')