"""
istitle(), isupper(), islower(), isspace(), isidentifier(), 'encode' code use
"""


str1 = "PYTHON!"
str2= " i love python!"
str3 = "I Love Python!"
str4 = " "
str5 = "monsurbiplob"
str6 = "5biplob"
str7 = "pyhton!"

num1 = '12345678'

# print(str1.istitle())
# print(str1.isupper())
# print(str2.islower())
# print(str4.isspace())
# print(str6.isidentifier())
# print(str6.encode())

print('Is all number: ', num1.isalnum())
print('Is alpha beta chracter: ', num1.isalpha())
print('Is ascii chracter: ', num1.isascii())
print('Is decimal chracter: ', num1.isdecimal())
print('Is digit: ', str2.isdigit())
print('Is numeric value: ', str1.isnumeric())
print('Is Printable values: ', str7.isprintable())