"""
Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers
(i.e. 0 yi  232, every value equally likely).
for the sequence xi the following recursion is given:x0 = 0 and
xi = xi-1| yi-1, for i  0. ( | is the bitwise-or operator)
it can be seen that eventually there will be an index n such that xi = 232 -1 (a bit-pattern of all ones) for all i  n.

find the expected value of n. 
give your answer rounded to 10 digits after the decimal point.
"""