from os import environ
from sys import stdin, stdout
from math import gcd
import numpy as np
from sympy import Matrix

class Hill:

    def __init__(self):
        self.N = 2
        self.M = 2
        self.MOD = 26

    def pair_to_matrix(self, txt):
        assert len(txt) == 2
        mtx = []
        mtx.append(ord(txt[0]) - ord('A'))
        mtx.append(ord(txt[1]) - ord('A'))
        return np.array(mtx).reshape((2, 1))

    def matrix_to_pair(self, matrix):
        # assert type(matrix) == type(Matrix([])) or type(matrix)==type(list())
        pair = ""
        pair += chr(matrix[0][0] + ord('A'))
        pair += chr(matrix[1][0] + ord('A'))
        return pair

    def encrypt(self, txt, key):

        key = np.array(key).reshape((self.N, self.M))

        if len(txt) & 1 > 0:
            txt += 'X'
        n = len(txt)
        mult = []
        
        for i in range(1, n, 2):
            element = (key @ self.pair_to_matrix(txt[i-1]+txt[i]) ) % self.MOD
            mult.append(element)

        output = ""
        for mtx in mult:
            output += self.matrix_to_pair(mtx)
        return output 

    def decrypt(self, encry, key):
        key = np.array(key).reshape((self.N, self.M))
        n = len(encry)
        mult = []
        for i in range(1, n, 2):
            element = (key @ self.pair_to_matrix(encry[i-1]+encry[i]) ) % self.MOD
            mult.append(element)
        output = ""
        for mtx in mult:
            output += self.matrix_to_pair(mtx)
        return output 

if __name__ == '__main__':
    key = [
        [3, 3],
        [2, 5]
    ]
    txt = "HELP"
    handle = Hill()
    encrypt = handle.encrypt(txt, key)
    print("Encrypt:", encrypt)
    key_inverse = np.array(Matrix(key).inv_mod(Hill().MOD))
    decrypt = handle.decrypt(encrypt, key_inverse)
    print("Decrypt:", decrypt)
