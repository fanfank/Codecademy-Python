n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(multi_list):
    lst = []
    for l in multi_list:
        for e in l:
            lst.append(e)
    return lst



print flatten(n)