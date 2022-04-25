import math


def monthly_payment():
    year = float(input("Enter year: "))
    principle = float(input("Enter Principle amount: "))
    rate_of_interest = float(input("Enter Rate of Interest: "))
    n = 12 * year
    r = (rate_of_interest / 12) * 100
    num = principle * r
    den = 1 - math.pow(1 + r, -n)
    payment = num / den
    print(f"Payment is {payment}")



if __name__=='__main__':

 monthly_payment()