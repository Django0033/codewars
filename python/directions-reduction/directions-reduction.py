def dirReduct(arr):
    directions_dict = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    res = []
    for i in arr:
        if res and res[-1] == directions_dict[i]:
            print('if {} {} {}'.format(i, res, res[-1]))
            res.pop()
        else:
            res.append(i)
            print('else {} {}'.format(i, res))
    return res
    

test1 = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
test2 = ['NORTH', 'WEST', 'SOUTH', 'EAST']

print(dirReduct(test1))
