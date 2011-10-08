"""
We call the convex area enclosed by two circles a lenticular hole if:
the centres of both circles are on lattice points.
the two circles intersect at two distinct lattice points.
the interior of the convex area enclosed by both circles does not contain any lattice points.

consider the circles:
c0: x2+y2=25
c1: (x+4)2+(y-4)2=1
c2: (x-12)2+(y-4)2=65


the circles c0, c1 and c2 are drawn in the picture below.


c0 and c1 form a lenticular hole, as well as c0 and c2.

we call an ordered pair of positive real numbers (r1, r2) a lenticular pair if there exist two circles with radii r1 and r2 that form a lenticular hole.
we can verify that (1, 5) and (5, 65) are the lenticular pairs of the example above.

let l(n) be the number of distinct lenticular pairs (r1, r2) for which 0  r1 r2 n.
we can verify that l(10) = 30 and l(100) = 3442.

find l(100 000).
"""