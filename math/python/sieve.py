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
