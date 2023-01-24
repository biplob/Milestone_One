user = {
    'id': 1,
    'first_name': 'Shajahan',
    'last_name' : 'Khan',
    'username' : 'admin',
    'password': '12345678',
    'role' : 'admin'
     }

# first_name = user['first_name']
# last_name = user['last_name']
# print(first_name, last_name)
# print(user['first_name'])
# print(user['last_name'])

# first_name = user.get('first_name')
# username = user.get('username')
# print(first_name, username)

key = user.keys()
values = user.values()
print((list(key)))
print(list(values))