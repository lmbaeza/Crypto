from os import environ
from sys import stdin, stdout
from math import gcd

class Vigenere:

    def encrypt(self, txt, key):
        mod = 26
        txt = txt.replace(" ", "")
        txt = txt.upper()
        n = len(txt)
        key_complete = ""
        m = len(key)
        for i in range(n):
            key_complete += key[(i % m)]
        
        output = ""
        for i in range(n):
            ord1 = ord(key_complete[i]) - ord('A')
            ord2 = ord(txt[i]) - ord('A')

            output += chr( ((ord1+ord2) % mod) + ord('A') )
        return output
            

    def decrypt(self, encry, key):
        mod = 26
        n = len(encry)
        key_complete = ""
        m = len(key)
        for i in range(n):
            key_complete += key[(i % m)]
        
        output = ""
        for i in range(n):
            ord1 = ord(key_complete[i]) - ord('A')
            ord2 = ord(encry[i]) - ord('A')
            output += chr( ((ord2-ord1) % mod) + ord('A') )
        return output

if __name__ == '__main__':
    algo = Vigenere()
    txt = "EL CURSo DE CRIPTOGRAFIA ME ENCANTA"
    key = "UNAL"
    encrypt = algo.encrypt(txt, key)
    print("Encrypt:", encrypt)
    decrypt = algo.decrypt(encrypt, key)
    print("Decrypt", decrypt)
