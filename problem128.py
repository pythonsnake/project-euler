"""
A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles, starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise direction.
new rings are added in the same fashion, with the next rings being numbered 8 to 19, 20 to 37, 38 to 61, and so on. the diagram below shows the first three rings.


by finding the difference between tile n and each its six neighbours we shall define pd(n) to be the number of those differences which are prime.
for example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 1, and 13. so pd(8) = 3.
in the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, hence pd(17) = 2.
it can be shown that the maximum value of pd(n) is 3.
if all of the tiles for which pd(n) = 3 are listed in ascending order to form a sequence, the 10th tile would be 271.
find the 2000th tile in this sequence.
"""