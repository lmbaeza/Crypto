random_device rd;
mt19937 gen(rd());

template<typename T>
T random(T from, T to) {
    if constexpr (is_integral<T>::value) {
        return uniform_int_distribution<T>(from, to)(gen);
    } else if constexpr (is_floating_point<T>::value) {
        return uniform_real_distribution<T>(from, to)(gen);
    } else {
        return uniform_int_distribution<T>(from, to)(gen);
    }
}
// shuffle(permutation.begin(), permutation.end(), gen);