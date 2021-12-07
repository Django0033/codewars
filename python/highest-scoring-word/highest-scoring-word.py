def high(x):
    score = {'a': 1, 'b': 2, '': 0, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    word = x.split()
    score_list = []
    for i in word:
        score_list.append(sum([score[j] for j in i]))

    return word[score_list.index(max(score_list))]

test1 = high('man i need a taxi up to ubud')
test2 = high('what time are we climbing up the volcano')
test3 = high('aa b')

print(test3)
