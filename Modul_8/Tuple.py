def area_volume(length, width, height):
    """
    retrun area and volume of any object
    """
    area = length * width
    volume = length * width * height
    return area, volume, length, width

# print(area_volume(2,3,5))
test = area_volume(2,3,5)
# print(test)
# print(type(test))
test_list = list(test)
print(test_list)
test_tup = tuple(test_list)
print(test_tup)

fruits = ("apple", "banana", "cherry")
x, y, z = fruits
print(z)