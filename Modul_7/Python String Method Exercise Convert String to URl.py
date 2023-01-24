# Write a Python funcation to convert string to url?



"""
convert it to lower case
replace blank space with -(dash)
convert it to funcation
"""
def urlfy(string):

    """
     The funcation will convert string to url

    :param string:
    :return: url
    """
    stripid_string = string.strip()
    lower_case = stripid_string.lower()
    url = lower_case.replace(' ', '-')
    return  url

print(urlfy('Hello Are You There? '))


def convert_url(str):
    """
    Write another funcation for understand. the funcation will convert string to url

    :param str:
    :return: url1
    """
    strip_less = str.strip()
    lower_case = strip_less.lower()
    url1 = lower_case.replace(' ', '---')
    return  url1

print(convert_url('Md Monsur Islam Bhuiyan '))
