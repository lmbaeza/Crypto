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