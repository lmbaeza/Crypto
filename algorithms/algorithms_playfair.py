from os import environ
from sys import stdin, stdout
from math import gcd

# En este alfabeto omotimos j

KEYS = [
    "IVANC",
    "BDEFG",
    "HKLMO",
    "PQRST",
    "UWXYZ"
]

def is_same_row(x, y):
    for row in KEYS:
        if x in row and y in row:
            return True
    return False


def is_same_col(x, y):
    n = len(KEYS)
    if n == 0: return False
    m = len(KEYS[0])
    
    for j in range(m):
        is_x, is_y = False, False
        for i in range(n):
            if KEYS[i][j] == x:
                is_x = True
            if KEYS[i][j] == y:
                is_y = True
        if is_x and is_y:
            return True
    return False

def find_position(char):
    n = len(KEYS)
    if n == 0: return -1, -1
    m = len(KEYS[0])
    
    for i in range(n):
        for j in range(m):
            if KEYS[i][j] == char:
                return i, j
    return -1, -1


class PlayFair:

    def encrypt(self, txt, DEBUG=False):
        txt = txt.replace(" ", "")
        cln_txt = txt[0]
        for i in range(1, len(txt), 1):
            if(txt[i-1] == txt[i]):
                cln_txt += 'X'
                cln_txt += txt[i]
            else:
                cln_txt += txt[i]
        txt = cln_txt
        
        if len(txt) & 1 > 0:
            txt += 'X';
        
        n = len(txt)
        pairs = []
        for i in range(0, n, 2):
            pairs.append((txt[i], txt[i+1]))
            if DEBUG: print(txt[i]+txt[i+1], end=" ")
        if DEBUG: print()
        
        # 1) Si ambas letras están en la misma fila, tomamos la letra a la derecha en la matriz
        # 2) Si ambas letras están en la misma columna, tomamos la letra debajo en la matriz
        # 3) Tomamos las letras en la intersección de la misma la y la otra columna
        output = ""

        n = len(KEYS)
        m = len(KEYS[0])

        for pair in pairs:
            char1, char2 = pair
            x1, y1 = find_position(char1)
            x2, y2 = find_position(char2)
            if is_same_row(char1, char2): # (1)
                y1 = (y1 + 1) % n
                y2 = (y2 + 1) % n
                output += KEYS[x1][y1]
                output += KEYS[x2][y2]
            elif is_same_col(char1, char2): # (2)
                x1 = (x1 + 1) % m
                x2 = (x2 + 1) % m
                output += KEYS[x1][y1]
                output += KEYS[x2][y2]
            else: # (3)
                output += KEYS[x1][y2]
                output += KEYS[x2][y1]
                
        return output

    def decrypt(self, encry):
        return None


if __name__ == '__main__':
    txt = "THIS IS AN INTERESTING BIG MESSAGE"
    handle = PlayFair()
    # tt = int(input())
    # for i in range(tt):
    #     handle.testing()
    encrypt = handle.encrypt(txt, DEBUG=True)
    print("Encrypt:", encrypt)
    decrypt = handle.decrypt(encrypt)
    print("Decrypt:", decrypt)
    

