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