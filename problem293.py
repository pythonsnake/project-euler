"""
An even positive integer n will be called admissible, if it is a power of 2 or its distinct prime factors are consecutive primes.
the first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.


if n is admissible, the smallest integer m  1 such that n+m is prime, will be called the pseudo-fortunate number for n.


for example, n=630 is admissible since it is even and its distinct prime factors are the consecutive primes 2,3,5 and 7. 
the next prime number after 631 is 641; hence, the pseudo-fortunate number for 630 is m=11.
it can also be seen that the pseudo-fortunate number for 16 is 3.


find the sum of all distinct pseudo-fortunate numbers for admissible numbers n less than 109.
"""