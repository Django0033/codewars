def high(x):
    '''
    Given a string of words, you need to find the highest scoring word.
    Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
    You need to return the highest scoring word as a string.
    If two words score the same, return the word that appears earliest in the original string.
    All letters will be lowercase and all inputs will be valid.
    '''

    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

test1 = high('man i need a taxi up to ubud')
test2 = high('what time are we climbing up the volcano')
test3 = high('aa b')

print(test3)
