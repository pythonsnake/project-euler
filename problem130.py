"""
A number consisting entirely of ones is called a repunit. we shall define r(k) to be a repunit of length k; for example, r(6) = 111111.
given that n is a positive integer and gcd(n, 10) = 1, it can be shown that there always exists a value, k, for which r(k) is divisible by n, and let a(n) be the least such value of k; for example, a(7) = 6 and a(41) = 5.
you are given that for all primes, p  5, that p  1 is divisible by a(p). for example, when p = 41, a(41) = 5, and 40 is divisible by 5.
however, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.
find the sum of the first twenty-five composite values of n for whichgcd(n, 10) = 1 and n  1 is divisible by a(n).
"""