def printer_error(s):
    return '{}/{}'.format(len([x for x in s if x not in 'abcdefghijklm']), len(s))

test1 = 'aaabbbbhaijjjm'
test2 = 'aaaxddddyyhwawiwjjjwwm'

print(printer_error(test1))
print(printer_error(test2))
