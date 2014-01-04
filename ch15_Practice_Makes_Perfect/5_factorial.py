def factorial(x):
    ans = 1
    while x > 0:
        ans *= x
        x -= 1
    return ans