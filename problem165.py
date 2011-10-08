"""
A segment is uniquely defined by its two endpoints. by considering two line segments in plane geometry there are three possibilities: 
the segments have zero points, one point, or infinitely many points in common.
moreover when two segments have exactly one point in common it might be the case that that common point is an endpoint of either one of the segments or of both. if a common point of two segments is not an endpoint of either of the segments it is an interior point of both segments.
we will call a common point t of two segments l1 and l2 a true intersection point of l1 and l2  if t is the only common point of l1 and l2  and t is an interior point of both segments.

consider the three segments l1, l2, and l3:
l1: (27, 44) to (12, 32)
l2: (46, 53) to (17, 62)
l3: (46, 70) to (22, 40)
it can be verified that line segments l2 and l3 have a true intersection point. we note that as the one of the end points of l3: (22,40) lies on l1 this is not considered to be a true point of intersection. l1 and l2 have no common point. so among the three line segments, we find one true intersection point.
now let us do the same for 5000 line segments. to this end, we generate 20000 numbers using the so-called "blum blum shub" pseudo-random number generator.
s0 = 290797
sn+1 = snsn (modulo 50515093)
tn = sn (modulo 500)
to create each line segment, we use four consecutive numbers tn. that is, the first line segment is given by:
(t1, t2) to (t3, t4)
the first four numbers computed according to the above generator should be: 27, 144, 12 and 232. the first segment would thus be (27,144) to (12,232).
how many distinct true intersection points are found among the 5000 line segments?
"""