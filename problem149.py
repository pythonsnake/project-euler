"""
Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).


253296513273184  8

now, let us repeat the search, but on a much larger scale:

first, generate four million pseudo-random numbers using a specific form of what is known as a "lagged fibonacci generator":

for 1 k  55, sk = [100003  200003k + 300007k3] (modulo 1000000)  500000.
for 56 k  4000000, sk = [sk24 + sk55 + 1000000] (modulo 1000000)  500000.

thus, s10 = 393027 and s100 = 86613.

the terms of s are then arranged in a 20002000 table, using the first 2000 numbers to fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on.

finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).
"""