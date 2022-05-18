from random import choice


class TemperatureConversion:

    def conversion(self, fahr, cel):
        option = int(input("Enter 1 or 2  :"))
        if option == 1:

            fahr = ((cel * 9) / 5) + 32
            print(f"{cel} celsius is {fahr} Fahrenheit")

        elif option == 2:
            cel = (fahr - 32) * 5.0 / 9.0
            print(f"{fahr} fahrenheit is {cel} celsius")


if __name__ == '__main__':
    temp = TemperatureConversion()
    temp.conversion(271, 271)
