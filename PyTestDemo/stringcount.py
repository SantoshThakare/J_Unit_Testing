

def frq_or_character(_mystr):

    op = {}
    for char in _mystr:
        if char in op:
            op[char] +=1
        else:
            op[char]=1
    return op

if __name__ == '__main__':
    _str = input("Enter the string : ")
    freq = freq_or_character(_str)
    print(freq)