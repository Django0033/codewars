def filter_int(l):
    return [x for x in l if isinstance(x, int)]

test1 = filter_int([1, 2, 'a', 'b'])
test2 = filter_int([1, 'a', 'b', 0, 15])
test3 = filter_int([1, 2, 'aasf', '1', '123', 123])

print(test1)
