years = [1990,1978,1945,2003,1989,2007,2010,2031,2045,2050]
i = 0

while i < len(years):
    if years[i] % 4 == 0:
        print(years[i], 'Is leaf years')
    i = i+1