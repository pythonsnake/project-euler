"""
2n binary digits can be placed in a circle so that all the n-digit clockwise subsequences are distinct.

for n=3, two such circular arrangements are possible, ignoring rotations:


for the first arrangement, the 3-digit subsequences, in clockwise order, are: 000, 001, 010, 101, 011, 111, 110 and 100.

each circular arrangement can be encoded as a number by concatenating the binary digits starting with the subsequence of all zeros as the most significant bits and proceeding clockwise. the two arrangements for n=3 are thus represented as 23 and 29:
00010111 2 = 23
00011101 2 = 29

calling s(n) the sum of the unique numeric representations, we can see that s(3) = 23 + 29 = 52.

find s(5).
"""