import pytest
from vending_machine import vending_machine_
from dayofweek_ import day_of_week
from monthly_payment import monthly_payment_
from square_root_ import square_root
from temperature_coversion import TemperatureConversion


def test_vending_machine():
    output = vending_machine_(70)
    expected = 2
    assert output == expected


def test_days_of_week():
    output = day_of_week(4, 1, 2022)
    expected = "Tuesday"
    assert output == expected


def test_monthly_payment():
    output = monthly_payment_(50000, 3, 6)
    expected = 249.164
    assert output == expected


def test_square_root():
    output = square_root(25)
    expected = 5
    assert output == expected


def test_temp_conversion():
    output = TemperatureConversion().conversion(271, 271)
    expected = (519.8, 132.77777777777777)
    assert output == expected
