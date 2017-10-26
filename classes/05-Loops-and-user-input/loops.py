def currency_converter(rate,euros):
    dollars=euros*rate
    return dollars

rate=input("Enter rate: ")
euros=input("Enter euros: ")

print(currency_converter(float(rate),float(euros)))
