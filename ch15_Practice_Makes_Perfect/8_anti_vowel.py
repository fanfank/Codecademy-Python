def is_vowel(c):
    c = c.lower()
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        return True
    else:
        return False

def anti_vowel(text):
    res = ""
    for i in range(0, len(text)):
        if not is_vowel(text[i]):
            res += text[i]
    return res