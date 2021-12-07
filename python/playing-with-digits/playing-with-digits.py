def dig_pow(n, p):
    n = [int(i) for i in str(n)]
    total = 0
    
    for i in range(len(n)):
        total = total + n[i]**(p+i)
    
    n = [str(i) for i in n]
    n = int(''.join(n))

    if total % n == 0:
        return total // n

    else:
        return -1

test1 = dig_pow(89, 1)
test2 = dig_pow(92, 1)
test3 = dig_pow(46288, 3)

print(test3)
