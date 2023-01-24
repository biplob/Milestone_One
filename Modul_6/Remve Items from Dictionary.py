cars = {
    'brand': 'Toyota',
    'model': 'Mustang',
    'year': 2010,
    'color': 'black'
     }
# print(cars.get('brand'))
# cars.update({'color': 'blue'})
# print(cars)
cars.pop('year')
print(cars)
cars.pop('color')
print(cars)