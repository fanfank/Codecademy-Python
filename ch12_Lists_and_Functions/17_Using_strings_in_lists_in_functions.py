n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(lst):
    string = ""
    for i in range(len(lst)):
        string += lst[i]
    return string


print join_strings(n)