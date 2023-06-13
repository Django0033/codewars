from re import sub
def printer_error(s):
    return '{}/{}'.format(len(sub('[a-m]', '', s)), len(s))

test1 = 'aaabbbbhaijjjm'
test2 = 'aaaxddddyyhwawiwjjjwwm'

print(printer_error(test1))
print(printer_error(test2))
