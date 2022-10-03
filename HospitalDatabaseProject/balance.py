def balance(payment,payment_made):
    if payment>payment_made:
        balance=payment-payment_made
        print("We demand you :{:,}".format(balance) )
    elif payment<payment_made:
        balance=payment_made-payment
        print("You have a balance of :{:,}".format(balance) )
    else:
        print("You have zero balance.")
    return balance