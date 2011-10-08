"""
For any positive integer k, a finite sequence ai of fractions xi/yi is defined by:
a1 = 1/k and
ai = (xi-1+1)/(yi-1-1) reduced to lowest terms for i>1.
when ai reaches some integer n, the sequence stops. (that is, when yi=1.)
define f(k) = n. 
for example, for k = 20:



1/20  2/19  3/18 = 1/6  2/5  3/4  4/3  5/2  6/1 = 6



so f(20) = 6.



also f(1) = 1, f(2) = 2, f(3) = 1 and σf(k3) = 118937 for 1 k  100.



find σf(k3) for 1 k  2106.
"""