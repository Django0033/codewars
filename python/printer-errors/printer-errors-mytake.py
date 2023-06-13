def printer_error(s):
    allowed_characters = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
    s_length = len(s)
    errors = 0

    for character in s:
        if character not in allowed_characters:
            errors += 1
    
    errors_rate = '{}/{}'.format(errors, s_length)
    return errors_rate


test1 = 'aaabbbbhaijjjm'
test2 = 'aaaxddddyyhwawiwjjjwwm'

print(printer_error(test1))
print(printer_error(test2))
