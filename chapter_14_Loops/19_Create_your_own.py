lst1 = [1, 3, 5, 8, 9]
lst2 = [1, 3, 5, 7, 9, 11]
for a, b in zip(lst1, lst2):
    if a != b:
        break;
    print a
else:
    print "Hi, impossible to execute me~"
