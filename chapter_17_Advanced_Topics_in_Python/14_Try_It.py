squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)