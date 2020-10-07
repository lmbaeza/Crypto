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
        pass

if __name__ == '__main__':
    task = Task()
    task.solveOne()
