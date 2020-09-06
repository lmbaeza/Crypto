# from math import gcd
# Usage:
#   ans = gcd(100, 54)

# Euclid's algorithm

def gcd(a, b):
    tmp = 0
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a
