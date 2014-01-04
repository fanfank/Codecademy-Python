import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    count += 1
    if num == 5:
        print "Sorry, you lose!"
        break
else:
    print "You win!"