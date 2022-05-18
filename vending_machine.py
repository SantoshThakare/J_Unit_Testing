import math
"""
Find the Fewest Notes to be returned for Vending Machine
a. Desc -> There is 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes which can be
returned by Vending Machine. Write a Program to calculate the minimum number
of Notes as well as the Notes to be returned by the Vending Machine as a
Change
b. I/P -> read the Change in Rs to be returned by the Vending Machine
c. Logic -> Use Recursion and check for largest value of the Note to return change
to get to minimum number of Notes.
d. O/P -> Two Outputs - one the number of minimum Note needed to give the
change and second list of Rs Notes that would given in the Change

"""

def vending_machine_(amount):

    list1 = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

    count = 0
    note = 0
    money = amount
    while amount > 1:
        if amount/list1[note] >= 1:
            a = amount/list1[note]
            print("Count {} and {} Rupee Notes".format(math.floor(a), list1[note]))
            amount = amount - math.floor(a) * list1[note]
            count = count + math.floor(a)

        else:
            note += 1

    return count

if __name__ == "__main__":
    cash = vending_machine(70)
