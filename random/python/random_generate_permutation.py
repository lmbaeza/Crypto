def generate_permutation(n, start):
    permutation = list(range(start, start+n))
    random.shuffle(permutation)
    return permutation