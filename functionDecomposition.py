def examination(rub_amount, currency):
    if (currency != 'USD') and (currency != 'CNY'):
        print("Расчёт не может быть совершён")

def rub_to_currency(rub_amount, currency):
    if (currency == 'USD'):
        USD(rub_amount)
    elif (currency == 'CNY'):
        CNY(rub_amount)
    elif (currency == None):
        USD(rub_amount)
    else:
        examination(rub_amount, currency)

def calculationUSD(rub_amount):
    a = rub_amount / 70.99
    return a

def calculationCNY(rub_amount):
    return 6.44 * calculationUSD(rub_amount)

def USD(rub_amount):
    print("было:", rub_amount, "RUB,", "стало:", calculationUSD(rub_amount), "USD")

def CNY(rub_amount):
    print("Конвертация USD")
    USD(rub_amount)
    print("было:", calculationUSD(rub_amount), "USD,", " стало:", calculationCNY(rub_amount), "CNY")

print(rub_to_currency(7200))
