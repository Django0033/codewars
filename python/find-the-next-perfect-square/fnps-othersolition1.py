def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1

test1 = 121
test2 = 625
test3 = 114

print(find_next_square(test1))
print(find_next_square(test2))
print(find_next_square(test3))
