def longest(a1, a2):
    a1 = [char for char in a1]
    a2 = [char for char in a2]

    return ''.join(sorted(set([*a1, *a2])))

test1 = longest("aretheyhere", "yestheyarehere")
test2 = longest("loopingisfunbutdangerous", "lessdangerousthancoding")
test3 = longest("inmanylanguages", "theresapairoffunctions")

print(test3)
