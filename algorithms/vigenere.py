from os import environ
from sys import stdin, stdout
from math import gcd

# Template

class Input:
    def read(self, func):
        return func(stdin.readline().strip())
    def readn(self, func):
        return list(map(func, stdin.readline().strip().split()))
    def readiter(self):
        return iter(stdin.readline().strip().split())
    def next(self, it, func):
        return func(next(it))

pin = Input() # Python Input (pin)
    
LOCAL = environ.get("LOCAL")

def local(func):
    def innerFunc(*args, **kwargs):
        if LOCAL: return func()
    return innerFunc

def testcases(func):
    def innerFunc(*args, **kwargs):
        T = pin.read(int)
        for tt in range(T):
            func(*args, **kwargs)
    return innerFunc

@local
def debug(*args):
    print(*args)

# End Template

class Task:
    @testcases
    def solveOne(self):
        algo = Vigenere()
        txt = "EL CURSO DE CRIPTOGRAFIA ME ENCANTA"
        key = "UNAL"
        encrypt = algo.encrypt(txt, key)
        print("Encrypt:", encrypt)
        decrypt = algo.decrypt(encrypt, key)
        print("Decrypt", decrypt)

class Vigenere:

    def encrypt(self, txt, key):
        mod = 26
        txt = txt.replace(" ", "")
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
    task = Task()
    task.solveOne()
