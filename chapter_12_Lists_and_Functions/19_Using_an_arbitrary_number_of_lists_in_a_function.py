m = [1, 2, 3]
n = [4, 5, 6]
o = [7, 8, 9]

# Update the below function to take
# an arbitrary number of arguments
def join_lists(*lst):
    for i in range(1, len(lst)):
        for j in range(len(lst[i])):
            lst[0].append(lst[i][j])
    return lst[0]


print join_lists(m, n, o)