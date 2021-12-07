
def get_sum(a, b):

    if a == b:
        return a

    elif a > b:
        return get_sum(b, a)

    else:
        return a + get_sum(a + 1, b)

print(get_sum(5, 1))

