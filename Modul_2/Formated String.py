# The Afghanistan country code 93 will allow you to call Afghanistan from another country.

country_name = input("Enter your country name: ")
country_code = input("Enter your country code: ")

# sentence = 'The '+ country_name + ' country code ' + country_code +' will allow you to call '+country_name+' from anouther country'
sentence = f'The {country_name} country code {country_code} will allow you to call {country_name} from another country'
print(sentence)