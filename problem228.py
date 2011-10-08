"""
Let sn be the regular n-sided polygon – or shape – whose vertices 

vk (k = 1,2,…,n) have coordinates:

    xk   =  
        cos( 2k-1/n180° )
  
    yk   =  
        sin( 2k-1/n180° )
  each sn is to be interpreted as a filled shape consisting of all points on the perimeter and in the interior.

the minkowski sum, s+t, of two shapes s and t is the result of 

adding every point in s to every point in t, where point addition is performed coordinate-wise: 

(u, v) + (x, y) = (u+x, v+y).

for example, the sum of s3 and s4 is the six-sided shape shown in pink below:




how many sides does s1864 + s1865 + … + s1909 have?
"""