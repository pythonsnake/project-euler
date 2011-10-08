"""
Given a set of points on a plane, we define a convex hole to be a convex polygon having as vertices any of the given points and not containing any of the given points in its interior (in addition to the vertices, other given points may lie on the perimeter of the polygon). 


as an example, the image below shows a set of twenty points and a few such convex holes. 
the convex hole shown as a red heptagon has an area equal to 1049694.5 square units, which is the highest possible area for a convex hole on the given set of points.





table.p252 td {
  padding: 0px 3px 0px 3px;
  vertical-align: bottom;
  text-align: left;
}
for our example, we used the first 20 points (t2k1, t2k), for k = 1,2,…,20, produced with the pseudo-random number generator:

s0
    = 
    290797 
  sn+1
    = 
    sn2 mod 50515093
  tn
    = 
    ( sn mod 2000 )  1000 
  


i.e. (527, 144), (488, 732), (454, 947), …


what is the maximum area for a convex hole on the set containing the first 500 points in the pseudo-random sequence? specify your answer including one digit after the decimal point.
"""