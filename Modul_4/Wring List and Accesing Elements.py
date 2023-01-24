list_one = ['Ali Ahamed', 34, True, 'New York']

# print(list_one[0], list_one[3], sep=',')
# print(list_one[0:4], sep=',')
# print(list_one[-1:-4], sep=',')

# John Doe is a man of 26 years old. he lives in kamruk kamakkha.
name = list_one[0]
age = list_one[1]
living_place = list_one[3]
is_male = list_one[2]

if is_male:
    pronoun = 'he'
    gender = 'man'

else:
    pronoun = 'she'
    gender = 'women'

sentence = f'{name} is a {gender} of {age} years old. {pronoun.title()} lives in {living_place}.'

print(sentence)