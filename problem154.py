"""
A triangular pyramid is constructed using spherical balls so that each ball rests on exactly three balls of the next lower level.

then, we calculate the number of paths leading from the apex to each position:
a path starts at the apex and progresses downwards to any of the three spheres directly below the current position.
consequently, the number of paths to reach a certain position is the sum of the numbers immediately above it (depending on the position, there are up to three numbers above it).
the result is pascal's pyramid and the numbers at each level n are the coefficients of the trinomial expansion 
(x + y + z)n.
how many coefficients in the expansion of (x + y + z)200000 are multiples of 1012?
"""