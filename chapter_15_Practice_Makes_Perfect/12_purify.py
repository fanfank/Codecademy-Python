def purify(lst):
    res = []
    for e in lst:
        if e % 2 == 0:
            res.append(e)
    return res