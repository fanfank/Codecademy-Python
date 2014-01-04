def remove_duplicates(lst):
    res = []
    for e in lst:
        if e not in res:
            res.append(e)
    return res