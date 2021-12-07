def reverse_words(text):

    words = text.split(' ')
    words = [word[::-1] for word in words]
    return ' '.join(words)

test1 = reverse_words('The quick brown fox jumps over the lazy dog')
test2 = reverse_words('apple')
test3 = reverse_words('a b c d')

print(test3)
