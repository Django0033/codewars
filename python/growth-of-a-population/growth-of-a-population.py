
def nb_year(p0, percentage, aug, p):
    count = 0
    if p0 >= p:
        return count
    else:
        while p0 < p:
            p0 = p0 + (p0 * percentage / 100) + aug
            count += 1
        return count
