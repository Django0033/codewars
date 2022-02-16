def solution(s):
    s = [char for char in s]
    for idx, char in enumerate(s):
        if char.isupper():
            s[idx] = ' ' + s[idx]
    return ''.join(s).strip()

test1 = solution('helloWorld')
test2 = solution('camelCase')
test3 = solution('breakCamelCase')

print(test3)
