"""
The radical of n, rad(n), is the product of distinct prime factors of n. for example, 504 = 23 32 7, so rad(504) = 2  3  7 = 42.
we shall define the triplet of positive integers (a, b, c) to be an abc-hit if:
gcd(a, b) = gcd(a, c) = gcd(b, c) = 1
a b
a + b = c
rad(abc) c
for example, (5, 27, 32) is an abc-hit, because:
gcd(5, 27) = gcd(5, 32) = gcd(27, 32) = 1
5  27
5 + 27 = 32
rad(4320) = 30  32
it turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c  1000, with c = 12523.
find c for c  120000.

note: this problem has been changed recently, please check that you are using the right parameters.
"""