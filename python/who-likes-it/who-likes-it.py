def likes(names):
    output = ''

    if len(names) == 0:
        output = 'no one likes this'

    elif len(names) == 1:
        output = names[0] + ' likes this'

    elif len(names) > 1 and len(names) < 4:

        for i in range(len(names) - 1):
            output = output + names[i] + ', '
        
        output = output[:-2]
        output = output + ' and ' + names[-1] + ' like this'

    else:

        for i in range(0, 2):
            output = output + names[i] + ', '
        
        output = output[:-2]
        output = output + ' and ' + str(len(names) - 2) + ' others like this'

    return output


empty_list = []
one_like = ['Peter']
two_likes = ['Peter', 'Alex']
three_likes = ['Peter', 'Alex', 'Mark']
four_likes = ['Peter', 'Alex', 'Mark', 'Max']

print(likes(four_likes))
