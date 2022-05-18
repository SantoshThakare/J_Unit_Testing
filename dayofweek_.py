import math


def day_of_week(m, d, y):
    list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    y0 = y - (14 - m) / 12
    x = y0 + y0 / 4 - y0 / 100 + y0 / 400
    m0 = m + 12 * ((14 - m) / 12) - 2
    d0 = (d + x + 31 * m0 / 12) % 7

    return list[math.floor(d0)]


if __name__ == "__main__":
    _date = day_of_week(4, 1, 2022)
    print(_date)
