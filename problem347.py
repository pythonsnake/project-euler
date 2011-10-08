"""
The largest integer  100 that is only divisible by both the primes 2 and 3 is 96, as 96=32*3=25*3.
for two distinct primes p and q let m(p,q,n) be the largest positive integer n only divisible
by both p and q and m(p,q,n)=0 if such a positive integer does not exist.


e.g. m(2,3,100)=96. 
m(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
also m(2,73,100)=0 because there does not exist a positive integer  100 that is divisible by both 2 and 73.


let s(n) be the sum of all distinct m(p,q,n).
s(100)=2262.


find s(10 000 000).
"""