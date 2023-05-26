from math import sqrt

def find_next_square(sq):
    current_perfect_square = sqrt(sq)
    if not current_perfect_square.is_integer():
        return -1
    next_perfect_square = (current_perfect_square + 1) ** 2
    return int(next_perfect_square)

test1 = 121
test2 = 625
test3 = 114

print(find_next_square(test1))
print(find_next_square(test2))
print(find_next_square(test3))
