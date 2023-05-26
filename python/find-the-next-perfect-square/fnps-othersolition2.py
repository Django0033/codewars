def find_next_square(sq):
    x = sq ** 0.5
    return -1 if x % 1 else (x + 1) ** 2


test1 = 121
test2 = 625
test3 = 114

print(find_next_square(test1))
print(find_next_square(test2))
print(find_next_square(test3))
