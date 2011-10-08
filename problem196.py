"""
Build a triangle from all positive integers in the following way:

 1
 2  3
 4  5  6
 7  8  9 1011 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 2829 30 31 32 33 34 35 3637 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63 64 65 66
. . .

each positive integer has up to eight neighbours in the triangle.

a set of three primes is called a prime triplet if one of the three primes has the other two as neighbours in the triangle.

for example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.

if row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
if row 9 is considered, it contains only one prime which is an element of some prime triplet: 37.

define s(n) as the sum of the primes in row n which are elements of any prime triplet.
then s(8)=60 and s(9)=37.

you are given that s(10000)=950007619.

find  s(5678027) + s(7208785).
"""