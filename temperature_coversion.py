from random import choice


class TemperatureConversion:
    print("Enter 1. Fahrenheit to celsius conversion  OR \n"
          "Enter 2. Celsius to Fahrenheit conversion")

    def conversion(self):

        option = int(input())
        if option == 1:
            cel = int(input("Enter value "))
            fahr = ((cel * 9) / 5) + 32
            print(f"{cel} celsius is {fahr} Fahrenheit")

        elif option == 2:
            fahr = int(input("Enter value "))
            cel = (fahr - 32) * 5.0/9.0
            print(f"{fahr} fahrenheit is {cel} celsius")


temp = TemperatureConversion()

if __name__ == '__main__':

    temp.conversion()