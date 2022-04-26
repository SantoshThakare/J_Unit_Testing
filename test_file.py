import pytest
from vending_machine import vending_machine_
from dayofweek_ import day_of_week
from monthly_payment import monthly_payment_

def test_vending_machine():


    output = vending_machine_(70)
    expected = 2
    assert output == expected


def test_days_of_week():

    output = day_of_week(4,1,2022)
    expected = "Tuesday"
    assert output == expected


def test_monthly_payment():

    output = monthly_payment_(50000, 3 , 6)
    expected = 249.164
    assert output == expected
