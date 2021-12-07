def likes(names):
    n = len(names)
    # Return a dictionary with all the possible answers. Keys are the respective number
    # of likes and the values are the respective answers.
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
    # [min(4, n)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2

empty_list = []
one_like = ['Peter']
two_likes = ['Peter', 'Alex']
three_likes = ['Peter', 'Alex', 'Mark']
four_likes = ['Peter', 'Alex', 'Mark', 'Max']

print(likes(four_likes))
