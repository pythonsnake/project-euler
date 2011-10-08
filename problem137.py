"""
Consider the infinite polynomial series af(x) = xf1 + x2f2 + x3f3 + ..., where fk is the kth term in the fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; that is, fk = fk1 + fk2, f1 = 1 and f2 = 1.
for this problem we shall be interested in values of x for which af(x) is a positive integer.
surprisingly af(1/2)
 = 
(1/2).1 + (1/2)2.1 + (1/2)3.2 + (1/2)4.3 + (1/2)5.5 + ...
 
 = 
1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
 
 = 
2
the corresponding values of x for the first five natural numbers are shown below.

xaf(x)
211
1/22
(132)/33
(895)/84
(343)/55

we shall call af(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 10th golden nugget is 74049690.
find the 15th golden nugget.
"""