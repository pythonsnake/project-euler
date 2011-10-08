"""
Abcd is a convex, integer sided quadrilateral with 1  ab  bc  cd  ad.
bd has integer length. o is the midpoint of bd. ao has integer length.
we'll call abcd a biclinic integral quadrilateral if ao = co  bo = do.

for example, the following quadrilateral is a biclinic integral quadrilateral:
ab = 19, bc = 29, cd = 37, ad = 43, bd = 48 and ao = co = 23.




let b(n) be the number of distinct biclinic integral quadrilaterals abcd that satisfy ab2+bc2+cd2+ad2n.
we can verify that b(10 000) = 49 and b(1 000 000) = 38239.


find b(10 000 000 000).
"""