"""
Let {a1, a2,..., an} be an integer sequence of length n such that:
a1 = 6
for all 1 i n : φ(ai) i+1) i i+1 1
let s(n) be the number of such sequences with ann.
for example, s(10) = 4: {6}, {6, 8}, {6, 8, 9} and {6, 10}.
we can verify that s(100) = 482073668 and s(10 000) mod 108 = 73808307.

find s(20 000 000) mod 108.

1 φ denotes euler's totient function.
"""