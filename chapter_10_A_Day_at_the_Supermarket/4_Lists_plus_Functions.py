# Write your function below!
def fizz_count(x):
    count = 0
    for e in x:
        if e == 'fizz':
            count += 1
    return count