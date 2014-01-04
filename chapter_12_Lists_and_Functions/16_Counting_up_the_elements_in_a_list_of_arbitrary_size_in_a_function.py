n = [3, 5, 7]

def total(lst):
    ans = 0.0
    for i in range(len(lst)):
        ans += lst[i]
    """
        # or you can use this for loop
        for e in lst:
        ans += e
        """
    return ans

print total(n)