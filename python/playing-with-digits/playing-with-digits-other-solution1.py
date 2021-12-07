def dig_pow(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += int(c)**(p + i)

    return int(s/n) if s % n == 0 else -1

test1 = dig_pow(89, 1)
test2 = dig_pow(92, 1)
test3 = dig_pow(46288, 3)

print(test3)
