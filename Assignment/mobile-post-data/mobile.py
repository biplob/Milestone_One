mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
usd = input('Enter USD Ammount: ')
usd_number = int(usd)
exchange_rate = mobile_data.get('exchnage_rate')
mobile_company_name = "Xiaomi Note"
country = 'China'
bdt = usd_number * exchange_rate

sentence = f'{mobile_company_name} 5 is made in {country}. The price is {usd_number} USD which is almost equal to {bdt} BDT'

print(sentence)


