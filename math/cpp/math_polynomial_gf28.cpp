#include <bits/stdc++.h>

using namespace std;

template<typename T>
T to_integer(string binary) {
    int n = int(binary.size());
    assert(is_integral<T>::value && n <= 64);
    T answer = 0;
    for(int i = 0; i < n; ++i) {
        if(binary[i] == '1')
            answer |= (1 << (n-i-1));
    }
    return answer;
}

template<typename T>
string int_to_binary(T number) {
    string ans="";
    assert(is_integral<T>::value);
    int n = 32;
    for(int i = 0; i < n; ++i) {
        ans.push_back( (((1 << i) & number) > 0) + '0');
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

template<typename T>
string int_to_hex(T number) {
    assert(is_integral<T>::value);
    stringstream stream;
    stream << hex << number;
    string result( stream.str() );
    return result;
}

template<typename T>
class PolynomialGF28 {
    // Galois Field GF(2^8)
public:
    T value;

    PolynomialGF28(T val) : value(val) {}
    PolynomialGF28(const PolynomialGF28<T> &p)  {
        value = p.value;
    }

    PolynomialGF28(string bin) {
        value = to_integer<T>(bin);
    }

    PolynomialGF28<T> operator+(PolynomialGF28<T> other) {
        return PolynomialGF28<T>(value ^ other.value);
    }

    PolynomialGF28<T> operator*(PolynomialGF28<T> other) {
        T answer = T(0);
        T aes_poly = 0x11B; // 100011011 -> x^8+x^4+x^3+x+1 ϵ Z_2[x]
        for (int i = 0; i < 8; i ++) {
            answer ^= value & -(other.value & 1);
            other.value >>= T(1);
            value <<= T(1);
            value ^= (aes_poly & -(value >> 8));
        }
        return PolynomialGF28<T>(answer);
    }

    PolynomialGF28<T> invert() {
        PolynomialGF28<T>answer(value);
        for (int i = 0; i < 6; i ++) {
            answer = answer * answer;
            answer = answer * PolynomialGF28<T>(value);
        }
        return answer*answer;
    }
    
    // Not Tested Yet
    PolynomialGF28<T> operator/(PolynomialGF28<T> other) {
        return PolynomialGF28<T>(value) * other.invert();
    }
    
    PolynomialGF28<T> power(int n) {
        PolynomialGF28<T> answer(1);
        PolynomialGF28<T> tmp(value);
        while (n > 0) {
            if (n & 1) {
                answer = answer * tmp;
            }
            tmp = tmp * tmp;
            n >>= 1;
        }
        return answer;
    }
};

// https://crypto.stackexchange.com/questions/48918/inverse-of-a-polynomial-using-long-division-over-gf256

template<typename T>
using poly = PolynomialGF28<T>;

int main() {
    
    poly<int> x1("10");
    
    for(int i = 0; i < 10; ++i) {
        poly<int> ans = x1.power(i);
        cout << i;
        cout << " " << int_to_hex(ans.value) << endl;
    }
    return 0;
}