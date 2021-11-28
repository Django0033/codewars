string = ''.lower()
x = 0
y = 1
isogram = False

if len(string) == 0:
    isogram = True

for character in string:
    print('For each character in string')
    for character in string:
        print('For each character in string')
        if string[x] != string[y]:
            print(x, y)
            print('Check if the character in the index x it\'s not equal to the character in index y')
            isogram = True
            print('Isogram is true.')
            if y < len(string) - 1:
                print('If y is lower than the length of string')
                y += 1
                print('Add 1 to y')
        else:
            print('Otherwise...')
            isogram = False
            print('Isogram is false.')
    if not isogram:
        break
    elif x < y-1:
        x += 1
        print('Add 1 to x')
        y = x + 1
        print('Set y to x + 1')

print(isogram)
