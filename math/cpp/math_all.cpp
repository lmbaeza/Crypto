template<class T>
bool is_prime(T number) {
    if(number <= 0) return false;
    else if(number <= 3) return true;
    if(number%2==0 || number%3==0) return false;
    for(T i = 5; i*i <= number; i += 6) {
        if(number%i==0 || number%(i+2)==0) {
            return false;
        }
    }
    return true;
}
// Time Complexity: O(sqrt(N)), Space Complexity:  O(1)
// usage:
//   int number = 210;
//   bool ans = is_prime(number);

template<class T>
vector<T> divisors(T number) {
    vector<T> solutions;
    // 1 <= i <= sqrt(number)
    for (T i = 1; i <= sqrt(number); ++i) {
        // if i is divisor of number
        if (number % i == 0) {
            if (number/i == i) {
                // if i*i == number
                solutions.push_back(i);
            } else {
                // x=i, y=number/i
                // if x*y==number
                solutions.push_back(i);
                solutions.push_back(number/i);
            }
        }
    }
    return solutions;
}
// usage:
//   int number = 100;
//   vector<int> ans = divisors<int>(number);

// Euclid's algorithm
template<class T>
T gcd(T a, T b) {
    T tmp = 0;
    while (b){
        tmp = a;
        a = b;
        b = tmp % b;
    }
    return a;
}
// usage:
//   int ans = gcd<int>(15, 25);

// Euclid's algorithm
template<class T>
T gcd(T a, T b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}
// usage:
//   int ans = gcd<int>(15, 25);

template<class T>
T lcm(T a, T b) {  
    return (a*b)/gcd<T>(a, b);  
}
// usage:
//   int ans = lcm<int>(15, 25);

template<class T>
vector<T> prime_factors(T number)  {
    vector<T> factors;
    while (number % 2 == 0) {
        factors.push_back(2);
        number = number / 2;
    }
    for (T i = 3; i*i <= number; i += 2) {
        while (number % i == 0) {
            factors.push_back(i);
            number = number / i; 
        }
    }
    if (number > 2)  {
        factors.push_back(number);
    }
    return factors;
}
// usage:
//   int n = 100;
//   vector<int> factors = prime_factors<int>(n);
//   {2, 2, 5, 5}
//   2*2*5*5 = 2^2 * 5^2 = 100

template<class T>
vector<T> sieve(T number) {
    vector<bool> is_prime(number+1, false);
    for(T i = 4; i <= number; i += 2) {
        is_prime[i] = true;
    }
    for(T prime = 3; prime <= number; prime += 2) {
        if(!is_prime[prime]) {
            for(int j = prime*2; j <= number; j += prime) {
                is_prime[j] = true;
            }
        }
    }
    vector<T> primes;
    for(T i = 2; i <= number; ++i) {
        if(!is_prime[i]) primes.push_back(i);
    }
    return primes;
}
// usage:
//   int n = 100;
//   vector<int> primes = sieve<int>(n);
//   {2, 3, 5, 7, ... 83, 89, 97}