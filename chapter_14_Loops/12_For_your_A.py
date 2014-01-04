s = "A bird in the hand..."

# Add your for loop
for c in s:
    if c == 'A' or c == 'a':
        print "X",
    else:
        print c,




#Don't delete this print statement!
print # fanfank thinks it's related to buffer issue, without this line, the content is left in the buffer and not printed