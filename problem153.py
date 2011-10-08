"""
As we all know the equation x2=-1 has no solutions for real x.

if we however introduce the imaginary number i this equation has two solutions: x=i and x=-i.

if we go a step further the equation (x-3)2=-4 has two complex solutions: x=3+2i and x=3-2i.
x=3+2i and x=3-2i are called each others' complex conjugate.

numbers of the form a+bi are called complex numbers.

in general a+bi and abi are each other's complex conjugate.
a gaussian integer is a complex number a+bi such that both a and b are integers.

the regular integers are also gaussian integers (with b=0).

to distinguish them from gaussian integers with b  0 we call such integers "rational integers."

a gaussian integer is called a divisor of a rational integer n if the result is also a gaussian integer.

if for example we divide 5 by 1+2i we can simplify  in the following manner:

multiply numerator and denominator by the complex conjugate of 1+2i: 12i.

the result is 
.

so 1+2i is a divisor of 5.

note that 1+i is not a divisor of 5 because .

note also that if the gaussian integer (a+bi) is a divisor of a rational integer n, then its complex conjugate (abi) is also a divisor of n.
in fact, 5 has six divisors such that the real part is positive: {1, 1 + 2i, 1  2i, 2 + i, 2 i, 5}.

the following is a table of all of the divisors for the first five positive rational integers:

n gaussian integer divisors
with positive real partsum s(n) of these

divisors111
21, 1+i, 1-i, 25
31, 34
41, 1+i, 1-i, 2, 2+2i, 2-2i,413
51, 1+2i, 1-2i, 2+i, 2-i, 512
for divisors with positive real parts, then, we have: .
for 1 n  105,  s(n)=17924657155.
what is  s(n) for 1 n  108?
"""