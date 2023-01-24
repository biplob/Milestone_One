laptops = [
    {'model': 'HP', 'Price': 30000, 'ram': '8GB'},
    {'model': 'Apple', 'Price': 150000, 'ram': '16GB'},
    ['Dell', '8GB'],
    {'model': 'Assus', 'Price': 80000, 'ram': '32GB'}

]

# Hp laptop price is 30000 BDT. It comes with 8GB Ram.


for laptop in laptops:
    try:
       print(f'{laptop.get("model")} laptop price is {laptop.get("Price")} BDT. It comes with {laptop.get("ram")} Ram.')
    except:
        pass