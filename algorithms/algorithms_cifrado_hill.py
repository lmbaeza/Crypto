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

def testcases(func):
    def innerFunc(*args, **kwargs):
        T = pin.read(int)
        for tt in range(T):
            func(*args, **kwargs)
    return innerFunc

# End Template

class Matrix(object):
    
    MOD = int(1e9 + 7)

    def __init__(self, args):
        if type(args) == type(list()):
            self.M = args
            self.row = len(self.M)
            self.col = 0
            if(self.row == 0): self.col = 0
            else: self.col = len(self.M[0])
        else:
            self.row = args[0]
            self.col = args[1]
            self.M = [ [ 0 for i in range(self.col) ] for j in range(self.row) ]
            if(len(args) == 3 and args[2] == True):
                for i in range(0, self.row): self.M[i][i] = 1;
    
    def __mul__(self, other):
        assert self.col==other.row
        product = Matrix( (self.row, other.col) )
        
        for i in range(0, self.row):
            for j in range(0, other.col):
                for k in range(0, self.col):
                    #product.M[i][j] =(product.M[i][j]+self.M[i][k]*other.M[k][j])%MOD
                    product.M[i][j] += self.M[i][k] * other.M[k][j]
                    
        return product
    
    def __add__(self, other):
        assert self.row==other.row and self.col==other.col
        ans = Matrix( (self.row, self.col) ) 
        
        for i in range(0, self.row):
            for j in range(0, self.col):
                #ans.M[i][j] = (self.M[i][j] + other.M[i][j]) % MOD
                ans.M[i][j] = self.M[i][j] + other.M[i][j]
        return ans
    
    def __sub__(self, other):
        assert self.row==other.row and self.col==other.col
        ans = Matrix( (self.row, self.col) ) 
        
        for i in range(0, self.row):
            for j in range(0, self.col):
                #ans.M[i][j] = (self.M[i][j] - other.M[i][j]) % MOD
                ans.M[i][j] = self.M[i][j] - other.M[i][j]
        return ans
    
    def __mod__(self, mod):
        assert type(mod) == type(int(1))
        for i in range(0, self.row):
            for j in range(0, self.col):
                self.M[i][j] = self.M[i][j] % mod
        return self
    
    def __repr__(self):
        return "Matrix<" + str(self.M) + ">"
    
# Usage:
# A = Matrix( [[1, 2], [3, 4]] )
# B = Matrix( [[4, 3], [2, 1]] )
# A+B, A-B, A*B

def pair_to_matrix(txt):
    assert len(txt) == 2
    mtx = [[], []]
    mtx[0].append(ord(txt[0]) - ord('A'))
    mtx[1].append(ord(txt[1]) - ord('A'))
    return Matrix(mtx)


def matrix_to_pair(matrix):
    assert type(matrix) == type(Matrix([[]])) or type(matrix)==type(list())
    M = []
    if type(matrix) == type(Matrix([[]])):
        M = matrix.M
    else:
        M = matrix
    pair = ""
    pair += chr(M[0][0] + ord('A'))
    pair += chr(M[1][0] + ord('A'))
    return pair

class Task:
    @testcases
    def solveOne(self):
        key = [
            [3, 3],
            [2, 5]
        ]
        txt = "HELP"
        handle = Hill()
        encrypt = handle.encrypt(txt, key)
        print("Encrypt:", encrypt)
        key_inverse = [
            [5/9, -1/3],
            [-2/9, 1/3]
        ]
        # Fail
        decrypt = handle.decrypt(encrypt, key)
        print("Decrypt:", decrypt)

class Hill:

    def encrypt(self, txt, key):
        if len(txt) & 1 > 0:
            txt += 'X'
        n = len(txt)
        mult = []
        key = Matrix(key)
        for i in range(1, n, 2):
            element = key * pair_to_matrix(txt[i-1]+txt[i])
            element = element % 26
            mult.append(element)

        output = ""
        for mtx in mult:
            output += matrix_to_pair(mtx)
        return output 


    def decrypt(self, encry, key):
        if len(encry) & 1 > 0:
            encry += 'X'
        n = len(encry)
        mult = []
        key = Matrix(key)
        for i in range(1, n, 2):
            element = key * pair_to_matrix(encry[i-1]+encry[i])
            element = element % 26
            mult.append(element)

        output = ""
        for mtx in mult:
            output += matrix_to_pair(mtx)
        return output 


if __name__ == '__main__':
    task = Task()
    task.solveOne()
