def delete_nth(order,max_e):
    new_list = []
    for i in order:
        if new_list.count(i) < max_e:
            new_list.append(i)
    return new_list
