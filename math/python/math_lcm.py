from math import gcd
def lcm(a, b):
    return (a*b)//gcd(a, b)

# usage:
#   ans = lcm(15, 25);