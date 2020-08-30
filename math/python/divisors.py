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