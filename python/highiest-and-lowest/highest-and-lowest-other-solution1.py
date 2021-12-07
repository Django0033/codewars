
def high_and_low(numbers):
    numbers_list = [int(i) for i in numbers.split()]

    return '{} {}'.format(max(numbers_list), min(numbers_list))

test1 = '8 3 -5 42 -1 0 0 -9 4 7 4 -4'
test2 = '1 2 3'

print(high_and_low(test1))
