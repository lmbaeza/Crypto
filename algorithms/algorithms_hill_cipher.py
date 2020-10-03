from os import environ
from sys import stdin, stdout
from math import gcd
import numpy as np
from sympy import Matrix

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

def testcases(func):
    def innerFunc(*args, **kwargs):
        T = pin.read(int)
        for tt in range(T):
            func(*args, **kwargs)
    return innerFunc

# End Template

N = 2
M = 2
MOD = 26

def pair_to_matrix(txt):
    assert len(txt) == 2
    mtx = []
    mtx.append(ord(txt[0]) - ord('A'))
    mtx.append(ord(txt[1]) - ord('A'))
    return np.array(mtx).reshape((2, 1))

def matrix_to_pair(matrix):
    # assert type(matrix) == type(Matrix([])) or type(matrix)==type(list())
    M = matrix
    pair = ""
    pair += chr(M[0][0] + ord('A'))
    pair += chr(M[1][0] + ord('A'))
    return pair

class Task:
    def solveOne(self):
        key = [
            [3, 3],
            [2, 5]
        ]
        txt = "HELP"
        handle = Hill()
        encrypt = handle.encrypt(txt, key)
        print("Encrypt:", encrypt)
        key_inverse = np.array(Matrix(key).inv_mod(MOD))
        decrypt = handle.decrypt(encrypt, key_inverse)
        print("Decrypt:", decrypt)

class Hill:

    def encrypt(self, txt, key):

        key = np.array(key).reshape((N, M))

        if len(txt) & 1 > 0:
            txt += 'X'
        n = len(txt)
        mult = []
        
        for i in range(1, n, 2):
            element = (key @ pair_to_matrix(txt[i-1]+txt[i]) ) % MOD
            mult.append(element)

        output = ""
        for mtx in mult:
            output += matrix_to_pair(mtx)
        return output 

    def decrypt(self, encry, key):
        key = np.array(key).reshape((N, M))
        n = len(encry)
        mult = []
        for i in range(1, n, 2):
            element = (key @ pair_to_matrix(encry[i-1]+encry[i]) ) % MOD
            mult.append(element)
        output = ""
        for mtx in mult:
            output += matrix_to_pair(mtx)
        return output 

if __name__ == '__main__':
    task = Task()
    task.solveOne()
