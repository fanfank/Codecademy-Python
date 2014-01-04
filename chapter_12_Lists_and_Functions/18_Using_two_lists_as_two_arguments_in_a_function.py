m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x, y):
    for i in range(len(y)):
        x.append(y[i])
    return x

print join_lists(m, n)