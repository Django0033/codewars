def high_and_low(numbers):
    numbers = numbers.split()
    numbers_list = []

    for i in numbers:
        numbers_list.append(int(i))

    return '{} {}'.format(max(numbers_list), min(numbers_list))

test1 = '8 3 -5 42 -1 0 0 -9 4 7 4 -4'
test2 = '1 2 3'

print(high_and_low(test1))
