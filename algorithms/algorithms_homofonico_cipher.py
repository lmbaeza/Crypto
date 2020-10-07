from os import environ
from sys import stdin, stdout
from math import gcd
import random

def random_int(from_value, to_value):
    return random.randrange(from_value, to_value+1)

TABLE = [
    [3,6,24,56,68,76, 83,86],            # A
    [10,29],                             # B
    [20, 45, 73],                        # C
    [26,35,55,61],                       # D
    [9,11,16,23,27,50,78,87,90,94,97],   # E
    [2,59],                              # F
    [17,32],                             # G
    [44,48,53,66,77,80],                 # H
    [18,38,51,63,72,92],                 # I
    [14],                                # J
    [37],                                # K
    [7,21,36,57],                        # L
    [12,39],                             # M
    [28,33,58,64,81,89],                 # N
    [40,46,60,84,93,96,99],              # O
    [0,31,67],                           # P
    [22],                                # Q
    [4,15,42,54,75,85],                  # R
    [34,62,65,74,79,91],                 # S
    [8,19,49,70,71,82,88,95, 98],        # T
    [43,52,69],                          # U
    [25],                                # V
    [13,30],                             # W
    [41],                                # X
    [1,47],                              # Y
    [5]                                  # Z
]

def to_str_number(number):
    assert 0 <= number and number <= 99
    if number >= 10:
        return str(number)
    else:
        return "0" + str(number)

class Homofonico:
    def encrypt(self, txt):
        n = len(txt)
        ans = ""
        for letter in txt:
            pos = ord(letter) - ord('A')
            value = random_int(0, len(TABLE[pos])-1)
            ans += str(to_str_number(TABLE[pos][value]))
        return ans

    def decrypt(self, encry):
        n = len(encry)
        ans = ""
        for i in range(0, n, 2):
            number = int(encry[i]+encry[i+1])
            for j in range(0, 26):
                if number in TABLE[j]:
                    ans += chr(j + ord('A'))
        return ans

if __name__ == '__main__':
    cipher = Homofonico()
    message = "STATISTICS ARE COMPLEX"
    message = message.replace(" ", "")
    encrypt = cipher.encrypt(message)
    print("Encrypt:", encrypt)
    decrypt = cipher.decrypt(encrypt)
    print("Decrypt:", decrypt)
