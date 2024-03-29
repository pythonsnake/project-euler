"""
A natural number, n, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: n = a1 + a2 + ... + ak = a1a2 ... ak.
for example, 6 = 1 + 2 + 3 = 1  2  3.
for a given set of size, k, we shall call the smallest n with this property a minimal product-sum number. the minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
k=2: 4 = 2  2 = 2 + 2k=3: 6 = 1  2  3 = 1 + 2 + 3k=4: 8 = 1  1  2  4 = 1 + 1 + 2 + 4k=5: 8 = 1  1  2  2  2  = 1 + 1 + 2 + 2 + 2k=6: 12 = 1  1  1  1  2  6 = 1 + 1 + 1 + 1 + 2 + 6
hence for 2k6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.
in fact, as the complete set of minimal product-sum numbers for 2k12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
what is the sum of all the minimal product-sum numbers for 2k12000?
"""