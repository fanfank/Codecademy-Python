from random import randrange

random_number = randrange(1, 10)

count = 0
# Start your game!
guess = int(raw_input("Enter a guess:"))
while guess != random_number:
    count += 1
    if count == 3:
        print "OMG! You lose! the answer is", str(random_number) + ", BB!"
        break
    guess = int(raw_input("Guess wrong, %s chance(s) left, enter a guess:" % (3 - count)))
else:
    print "OMG! You win! GB!"