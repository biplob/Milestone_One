user_name = 'biplob'
password = '12345'

input_user = input('Enter your user name: ')
input_password = input('Enter your password: ')

# if input_user == user_name and input_password == password:
#     print('You have a sucessfully login.')
# else:
#     print('Some thing went to wrong')

if input_user != user_name or input_password != password:
    print('Some thing went to wrong')

else:
    print('You have a sucessfully login.')