"""
A composite number can be factored many different ways.  
for instance, not including multiplication by one, 24 can be factored in 7 distinct ways:

24 = 2x2x2x3
24 = 2x3x4
24 = 2x2x6
24 = 4x6
24 = 3x8
24 = 2x12
24 = 24

recall that the digital root of a number, in base 10, is found by adding together the digits of that number, 
and repeating that process until a number is arrived at that is less than 10.  
thus the digital root of 467 is 8.
we shall call a digital root sum (drs) the sum of the digital roots of the individual factors of our number.
 the chart below demonstrates all of the drs values for 24.
factorisationdigital root sum2x2x2x3
92x3x4
92x2x6
104x6
103x8
112x12
524
6the maximum digital root sum  of 24 is 11.
the function mdrs(n) gives the maximum digital root sum of n. so  mdrs(24)=11.
find mdrs(n) for 1 n  1,000,000.
"""