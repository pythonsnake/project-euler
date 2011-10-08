"""
For fixed integers a, b, c, define the crazy function f(n) as follows:
f(n) = n - c for all n  b 
f(n) = f(a + f(a + f(a + f(a + n)))) for all n  b.


also, define s(a, b, c) = .


for example, if a = 50, b = 2000 and c = 40, then f(0) = 3240 and f(2000) = 2040.
also, s(50, 2000, 40) = 5204240.


find the last 9 digits of s(217, 721, 127).
"""