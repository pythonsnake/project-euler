"""
For two positive integers a and b, the ulam sequence u(a,b) is defined by u(a,b)1 = a, u(a,b)2 = b and for k > 2,
u(a,b)k is the smallest integer greater than u(a,b)(k-1) which can be written in exactly one way as the sum of two distinct previous members of u(a,b).
for example, the sequence u(1,2) begins with
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations as the sum of two previous members, likewise 7 = 1 + 6 = 3 + 4.
find u(2,2n+1)k for 2 n 10, where k = 1011.
"""