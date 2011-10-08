"""
Let a and b be bit strings (sequences of 0's and 1's).
if a is equal to the leftmost length(a) bits of b, then a is said to be a prefix of b.
for example, 00110 is a prefix of 001101001, but not of 00111 or 100110.

a prefix-free code of size n is a collection of n distinct bit strings such that no string is a prefix of any other.  for example, this is a prefix-free code of size 6:

0000, 0001, 001, 01, 10, 11

now suppose that it costs one penny to transmit a '0' bit, but four pence to transmit a '1'.
then the total cost of the prefix-free code shown above is 35 pence, which happens to be the cheapest possible for the skewed pricing scheme in question.
in short, we write cost(6) = 35.

what is cost(109) ?
"""