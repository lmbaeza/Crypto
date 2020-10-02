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

class Task:
    @testcases
    def solveOne(self):
        data = pin.read(str)
        n = len(data)
        LEN_ALPHA = 26
        target = 'lmba'
        for letter in range(LEN_ALPHA):
            new_str = ""
            for ch in data:
                new_str += chr( ( (ord(ch)-ord('a'))+letter) % LEN_ALPHA + ord('a') )
            
            if new_str == target:
                print("YES:", new_str, "->", data)


if __name__ == '__main__':
    task = Task()
    task.solveOne()

