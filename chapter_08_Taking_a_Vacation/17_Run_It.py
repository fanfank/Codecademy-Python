def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
    balance = add_monthly_interest(balance - payment)
    print "You still owe:", balance
    return balance

print make_payment(bill / 2 + 100, bill)
