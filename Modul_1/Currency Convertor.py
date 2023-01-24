usd = input('Enter usd Ammount: ')
usd_number = int(usd)
exchange_rate = 104
bdt = usd_number  * exchange_rate

# print(usd_number, 'is equal to', bdt, 'BDT')

paragraph = str(usd_number) + ' is equal to ' + str(bdt) + ' BDT'
print(paragraph)
