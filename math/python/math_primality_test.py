from math import sqrt
def is_prime_slow(number):
    if number <= 1: return False
    elif number <= 3: return True
    if number%2==0 or number%3==0: return False
    i = 5
    while i*i <= number:
        if number % i == 0 or number % (i+2) == 0:
            return False;
    # Time Complexity: O(sqrt(N)), Space Complexity:  O(1)
    return True


def zeros_right(n): # Similar to __builtin_ctzll in c++
    zeros = 0
    cnt = 0
    while True:
        mask = 1 << cnt
        if (n & mask) == 0:
            zeros += 1
        else:
            break
        cnt += 1
    return zeros

def witness(n, s, d, a):
    cur = 1
    p = d
    while p > 0:
        if (p & 1) > 0:
            cur = (cur*a) % n;
        a = (a*a)%n
        p >>= 1
    if cur == 1:
        return p, False
    for r in range(s):
        if cur == (n-1):
            return p, False
        cur = (cur*cur)%n
    return p, True

def miller_rabin(n, bases):
    n = int(n)
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for x in small_primes:
        if n == x:
            return True
        if n % x == 0:
            return False
    if n < 31*31:
        return False
    s = zeros_right(n-1)
    d = (n - 1) >> s
    for a in bases:
        if a % n == 0:
            return True
        d, answer = witness(n, s, d, a)
        if answer:
            return False
    return True

def is_prime(n):
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    return miller_rabin(n, bases)
