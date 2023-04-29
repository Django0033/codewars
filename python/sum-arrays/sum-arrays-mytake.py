def array_sum(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum

test1 = [1, 5.2, 4, 0, -1]
test2 = []
test3 = [-2.398]

print(array_sum(test1))
print(array_sum(test2))
print(array_sum(test3))
