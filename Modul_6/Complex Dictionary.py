users = [
    {'username': 'Golam Kibria',
     'password': '145sdthe',
     'role': 'admin'
     },

    {'username': 'Kairul Amin',
     'password': '1488_sfth_sf',
     'role': 'contibutor'},

]

for user in users:
    print(user.get('username'), user.get('password'), sep=", ")