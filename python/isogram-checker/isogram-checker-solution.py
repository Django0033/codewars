def is_isogram(string):
    string = string.lower()
    print('set string to lower')
    for letter in string:
        print('For each letter in string...')
        letter_count = string.count(letter)
        print('Set letter_count to string.count(letter)')
        print(letter_count)
        if letter_count > 1:
            print('Check if count leter is greater than 1')
            print('False')
            return False
        print('True')
        return True

is_isogram('ada')
