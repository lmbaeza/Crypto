from math import sqrt
def is_prime(number):
    if number <= 1: return False
    elif number <= 3: return True
    if number%2==0 or number%3==0: return False
    for i in range(5, int(sqrt(number))+1):
        if number % i == 0 or number % (i+2) == 0:
            return False;
    return True

# Time Complexity: O(sqrt(N)), Space Complexity:  O(1)
#  usage:
#   number = 210;
#   ans = is_prime(number);

from math import sqrt
def divisors(number: int) -> List[int]:
    solutions = []
    number = int(number)
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            if number // i == i:
                solutions.append(i)
            else:
                solutions.append(i)
                solutions.append(number // i)
    return solutions

# Time Complexity: O(sqrt(N)), Space Complexity:  O(N)
#  usage:
#   number = 100;
#   ans = divisors(number) # [1, 100, 2, 50, 4, 25, 5, 20, 10]

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


from math import gcd
def lcm(a, b):
    return (a*b)//gcd(a, b)

# usage:
#   ans = lcm(15, 25);

import math 
def prime_factors(n): 
    factors = []
    while n % 2 == 0: 
        factors.append(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            factors.append(i)
            n = n // i 
    if n > 2: 
        factors.append(n)
    return factors

# Time Complexity: O(sqrt(N)), Space Complexity:  O(N)
# usage:
#   n = 100;
#   factors = prime_factors(n);
#   {2, 2, 5, 5}
#   2*2*5*5 = 2^2 * 5^2 = 100

def sieve(number):
    prime = [True for i in range(number+1)]
    p = 2
    while (p * p <= number):
        if (prime[p] == True):
            for i in range(p * p, number+1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, number+1):
        if prime[p]:
            primes.append(p)
    return primes

# Time Complexity: O(N*log2(log2(N))), Space Complexity:  O(N)
# usage:
#   n = 100;
#   primes = sieve(n);
#   {2, 3, 5, 7, ... 83, 89, 97}

def xgcd(a, b):
    if b == 0:
        return a, 1, 0
    x, xtmp, y, ytmp = 1, 0, 0, 1
    while b != 0:
        q = a // b
        r = a - b * q
        u = x - q * xtmp
        v = y - q * ytmp
        # Update a, b
        a = b
        b = r
        # Update for next iteration
        x = xtmp
        xtmp = u
        y = ytmp
        ytmp = v
    return  a, x, y

# Space Complexity:  O(1)
#  a*x + b*y = gcd(a, b)
#  g = gcd(a, b)
# Usage:
#  g, x, y = xgcd(a, b)
