def check_bit4(num):
    if num & 0b1000 > 0:
        return "on"
    else:
        return "off"