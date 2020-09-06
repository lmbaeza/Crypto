template<typename T>
vector<T> random_permutation(int n, T start = 0) {
    vector<T> permutation(n);
    iota(permutation.begin(), permutation.end(), start);
    shuffle(permutation.begin(), permutation.end(), gen);
    return permutation;
}