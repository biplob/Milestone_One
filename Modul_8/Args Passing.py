# def add(a,b):
#     """
#     return total of two value
#     """
#
#     total = a + b
#     return total

# print(add(4, 6))

def multipul_arg(*args):
    total = 1
    for number in args:
        total = total * number
        # total += number
    return total

result = multipul_arg(1,2,4,5,6,7,8,9)
print(result)