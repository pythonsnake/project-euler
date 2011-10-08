"""
A root or zero of a polynomial p(x) is a solution to the equation p(x) = 0. 
define pn as the polynomial whose coefficients are the digits of n.
for example, p5703(x) = 5x3 + 7x2 + 3.

we can see that:pn(0) is the last digit of n,
pn(1) is the sum of the digits of n,
pn(10) is n itself.define z(k) as the number of positive integers, n, not exceeding k for which the polynomial pn has at least one integer root.

it can be verified that z(100 000) is 14696.

what is z(1016)?
"""