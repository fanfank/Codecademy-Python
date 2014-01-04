def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def get_min(balance, rate):
    return balance * rate

print get_min(bill, 0.02)