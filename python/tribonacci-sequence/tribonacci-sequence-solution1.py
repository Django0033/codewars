def tribonacci(signature, n):
    tribonacci_list = signature[:n]
    for _ in range (n - 3):
        tribonacci_list.append(sum(tribonacci_list[-3:]))
    return tribonacci_list

test1 = ([1, 1, 1], 10)
test2 = ([0, 0, 1], 10)
test3 = ([0, 1, 1], 10)
test4 = ([0, 1, 1], 0)
test5 = ([0, 1, 1], 1)
test6 = ([0, 1, 1], 2)
test7 = ([0, 1, 1], 3)

print(tribonacci(test1[0], test1[1]))
print(tribonacci(test2[0], test2[1]))
print(tribonacci(test3[0], test3[1]))
print(tribonacci(test4[0], test4[1]))
print(tribonacci(test5[0], test5[1]))
print(tribonacci(test6[0], test6[1]))
print(tribonacci(test7[0], test7[1]))
