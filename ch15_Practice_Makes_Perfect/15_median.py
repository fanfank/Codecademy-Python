def median(lst):
    lst2 = sorted(lst)
    length = len(lst2)
    if length % 2 == 0:
        return (lst2[length / 2] + lst2[length / 2 - 1]) / 2.0
    else:
        return lst2[length / 2]