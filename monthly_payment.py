import math


def monthly_payment_(principal_loan, year, rate):

    n = 12 * year
    r = rate/(12 * 100)
    payment = (principal_loan * r) / 1 - math.pow((1 + r), -n)
    return round(payment, 3)


if __name__ == "__main__":
    amount_required = monthly_payment_(50000, 3 , 6)
    print(amount_required)