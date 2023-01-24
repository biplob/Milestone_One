# a = 2
# square = a * a
# print(square)

def square(a):
    """
    return square of number

    :param a: any number
    :return: return value
    """
    value = a * a
    return  value

# print(square(5))

def multiplay(a, b):
    """
    return multiply of the number
    :param a:  a value
    :param b:  b value
    :return:  return value of total multiply
    """
    value = a * b
    return value
# print(multiplay(5, 6))

def multipul_args(*args):

    """
    return multiplu arguments of values.
    :param args: any type of value
    :return: return value
    """
    value = 1
    for number in args:
        value = value * number
    return value

result = multipul_args(4,5,6,7,8)
# print(result)
# print(result.__doc__)