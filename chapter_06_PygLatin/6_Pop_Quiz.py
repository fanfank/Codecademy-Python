print "Welcome to the English to Pig Latin translator!"
original = raw_input("What's your name?")
if len(original) != 0 and original.isalpha():
    print original
else:
    print "empty"