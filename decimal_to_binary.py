class DecimalToBinary:

    def dec_to_bin(self, num):
        if num >= 1:
            self.dec_to_bin(num // 2)
        print(num % 2, end='')


if __name__ == '__main__':

    dec_val = int(input("Enter number :"))
    con = DecimalToBinary()
    con.dec_to_bin(dec_val)