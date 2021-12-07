def reverse_words(text):
    return ' '.join(s[::-1] for s in text.split(' '))

test1 = reverse_words('The quick brown fox jumps over the lazy dog')
test2 = reverse_words('apple')
test3 = reverse_words('a b c d')

print(test1)
