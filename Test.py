

import vending_machine


def Vending_Machine_TestCall():

    output = vending_machine.vendingMachine(2000)
    expected = 2
    assert output == expected
