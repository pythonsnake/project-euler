"""
Four points with integer coordinates are selected:a(a, 0), b(b, 0), c(0, c) and d(0, d), 
with 0  a  b and 0  c  d.
point p, also with integer coordinates, is chosen on the line ac so that the three triangles abp, cdp and bdp are all similar.

it is easy to prove that the three triangles can be similar, only if a=c.

so, given that a=c, we are looking for triplets (a,b,d) such that at least one point p (with integer coordinates) exists on ac, making the three triangles abp, cdp and bdp all similar.

for example, if (a,b,d)=(2,3,4), it can be easily verified that point p(1,1) satisfies the above condition. 
note that the triplets (2,3,4) and (2,4,3) are considered as distinct, although point p(1,1) is common for both.

if b+d  100, there are 92 distinct triplets (a,b,d) such that point p exists.
if b+d  100 000, there are 320471 distinct triplets (a,b,d) such that point p exists.
if b+d  100 000 000, how many distinct triplets (a,b,d) are there such that point p exists?
"""