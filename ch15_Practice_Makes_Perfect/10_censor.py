"""
method 1: normal way to finish this task
"""
def censor(text, word):
    strings = text.split()
    for i in range(0, len(strings)):
        if strings[i] == word:
            strings[i] = "*" * len(word)
    return " ".join(strings)




"""
method 2: use KMP algorithm, but it's like employing a steam engine to crack a nut
"""
def get_next_array(word):
    nxt = [-1]
    for i in range(1, len(word)):
        n = nxt[i - 1]
        nxt.append(-1)
        while n != -1:
            if word[n + 1] == word[i]:
                nxt[i] = n + 1
                break
            n = nxt[n]
        if n == -1 and word[0] == word[i]:
            nxt[i] = 0
    return nxt

def KMP(text, word, nxt, i):
    j = 0
    while i < len(text) and j < len(word):
        while j != -1 and text[i] != word[j]:
            if j == 0:
                j = -1
            else:
                j = nxt[j-1] + 1
        i += 1
        j += 1
    if j == len(word):
        return i
    return -1

def censor(text, word): #use KMP algorithm
    nxt = get_next_array(word)
    i = 0
    while i < len(text) and i != -1:
        i = KMP(text, word, nxt, i)
        if i == -1:
            break;
        newtext = text[0: i - len(word)] + "*" * len(word) + text[i :]
        text = newtext
    return text