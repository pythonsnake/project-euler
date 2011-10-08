"""
A program written in the programming language fractran consists of a list of fractions.

the internal state of the fractran virtual machine is a positive integer, which is initially set to a seed value. each iteration of a fractran program multiplies the state integer by the first fraction in the list which will leave it an integer.

for example, one of the fractran programs that john horton conway wrote for prime-generation consists of the following 14 fractions:1791
,
7885
,
1951
,
2338
,
2933
,
7729
,
9523
,
7719
,
117
,
1113
,
1311
,
152
,
17
,
551
.
starting with the seed integer 2, successive iterations of the program produce the sequence:
15, 825, 725, 1925, 2275, 425, ..., 68, 4, 30, ..., 136, 8, 60, ..., 544, 32, 240, ...

the powers of 2 that appear in this sequence are 22, 23, 25, ...
it can be shown that all the powers of 2 in this sequence have prime exponents and that all the primes appear as exponents of powers of 2, in proper order!

if someone uses the above fractran program to solve project euler problem 7 (find the 10001st prime), how many iterations would be needed until the program produces 210001st prime ?
"""