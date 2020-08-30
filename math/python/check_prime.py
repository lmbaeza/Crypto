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