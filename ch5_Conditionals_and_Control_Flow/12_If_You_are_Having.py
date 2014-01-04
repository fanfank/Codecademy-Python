def using_control_once():
    if 1 == 1:
        return "Success #1"

def using_control_again():
    if not False:
        return "Success #2"

print using_control_once()
print using_control_again()