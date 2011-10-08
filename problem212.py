"""
An axis-aligned cuboid, specified by parameters { (x0,y0,z0), (dx,dy,dz) }, consists of all points (x,y,z) such that x0 x  x0+dx, y0 y  y0+dy and z0 z  z0+dz.  the volume of the cuboid is the product, dx  dy  dz.  the combined volume of a collection of cuboids is the volume of their union and will be less than the sum of the individual volumes if any cuboids overlap.

let c1,...,c50000 be a collection of 50000 axis-aligned cuboids such that cn has parameters

x0 = s6n-5 modulo 10000y0 = s6n-4 modulo 10000z0 = s6n-3 modulo 10000dx = 1 + (s6n-2 modulo 399)dy = 1 + (s6n-1 modulo 399)dz = 1 + (s6n modulo 399)

where s1,...,s300000 come from the "lagged fibonacci generator":

for 1 k  55, sk = [100003 - 200003k + 300007k3]   (modulo 1000000)for 56 k, sk = [sk-24 + sk-55]   (modulo 1000000)

thus, c1 has parameters {(7,53,183),(94,369,56)}, c2 has parameters {(2383,3563,5079),(42,212,344)}, and so on.

the combined volume of the first 100 cuboids, c1,...,c100, is 723581599.

what is the combined volume of all 50000 cuboids, c1,...,c50000 ?
"""