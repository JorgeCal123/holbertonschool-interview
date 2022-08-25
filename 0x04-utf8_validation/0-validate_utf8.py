#!/usr/bin/python3
"""method vald UTF8"""


def validUTF8(data):
    """
     method that determines if a given data set
     represents a valid UTF-8 encoding
    """
    n = 0
    for byte in data:
        binary = format(byte, '#010b')[-8:]
        if n == 0:
            for bit in binary:
                if bit == '0':
                    break
                n += 1
            if n == 0:
                continue
            if n == 1 or n > 4:
                return False
        else:
            if not (binary[0] == '1' and binary[1] == '0'):
                return False
        n = n - 1
    if not n:
        return True
    else:
        return False
