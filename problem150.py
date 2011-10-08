"""
In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible.
in the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of 42.


we wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers sk in the range 219, using a type of random number generator (known as a linear congruential generator) as follows:
t := 0

for k = 1 up to k = 500500:

    t := (615949*t + 797807) modulo 220
    sk := t219
thus: s1 = 273519, s2 = 153582, s3 = 450905 etc
our triangular array is then formed using the pseudo-random numbers thus:

s1
s2  s3
s4  s5  s6  

s7  s8  s9  s10
...

sub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements directly below it from the next row, the three elements directly below from the row after that, and so on).

the "sum of a sub-triangle" is defined as the sum of all the elements it contains.

find the smallest possible sub-triangle sum.
"""