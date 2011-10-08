"""
Starting from zero the natural numbers are written down in base 10 like this:

0 1 2 3 4 5 6 7 8 9 10 11 12....

consider the digit d=1. after we write down each number n, we will update the number of ones that have occurred and call this number f(n,1). the first values for f(n,1), then, are as follows:

nf(n,1)
00
11
21
31
41
51
61
71
81
91
102
114
125

note that f(n,1) never equals 3.

so the first two solutions of the equation f(n,1)=n are n=0 and n=1. the next solution is n=199981.
in the same manner the function f(n,d) gives the total number of digits d that have been written down after the number n has been written.

in fact, for every digit d  0, 0 is the first solution of the equation f(n,d)=n.
let s(d) be the sum of all the solutions for which f(n,d)=n.

you are given that s(1)=22786974071.
find  s(d) for 1  d  9.
note: if, for some n, f(n,d)=n
 for more than one value of d this value of n is counted again for every value of d for which f(n,d)=n.
"""