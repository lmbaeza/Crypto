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
        assert(self.col==other.row);
        product = Matrix( (self.row, other.col) )
        
        for i in range(0, self.row):
            for j in range(0, other.col):
                for k in range(0, self.col):
                    #product.M[i][j] =(product.M[i][j]+self.M[i][k]*other.M[k][j])%MOD
                    product.M[i][j] += self.M[i][k] * other.M[k][j]
        return product
    
    def __add__(self, other):
        assert(self.row==other.row and self.col==other.col)
        ans = Matrix( (self.row, self.col) ) 
        
        for i in range(0, self.row):
            for j in range(0, self.col):
                #ans.M[i][j] = (self.M[i][j] + other.M[i][j]) % MOD
                ans.M[i][j] = self.M[i][j] + other.M[i][j]
        return ans
    
    def __sub__(self, other):
        assert(self.row==other.row and self.col==other.col)
        ans = Matrix( (self.row, self.col) ) 
        
        for i in range(0, self.row):
            for j in range(0, self.col):
                #ans.M[i][j] = (self.M[i][j] - other.M[i][j]) % MOD
                ans.M[i][j] = self.M[i][j] - other.M[i][j]
        return ans
    
    def __repr__(self):
        return "Matrix<" + str(self.M) + ">"
    
# Usage:
# A = Matrix( [[1, 2], [3, 4]] )
# B = Matrix( [[4, 3], [2, 1]] )
# A+B, A-B, A*B

def pair_to_matrix(txt):
    assert len(txt) == 2


def matrix_to_pair(matrix):
    assert type(matrix) == type(Matrix) or type(matrix)==type(list())
    M = []
    if type(matrix) == type(Matrix):
        M = matrix.M
    else:
        M = matrix
    

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
        decrypt = handle.decrypt(encrypt, key)
        print("Decrypt:", decrypt)

class Hill:

    def encrypt(self, txt, key):
        if len(txt) & 1 > 0:
            txt += 'X'
        
        n = len(txt)
        output = ""
        for i in range(0, n, 2):
            pass

    def decrypt(self, encry, key):
        return None

if __name__ == '__main__':
    task = Task()
    task.solveOne()
