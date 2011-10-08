"""
A rectangular sheet of grid paper with integer dimensions w h is given. its grid spacing is 1.
when we cut the sheet along the grid lines into two pieces and rearrange those pieces without overlap, we can make new rectangles with different dimensions.
for example, from a sheet with dimensions 9  4 , we can make rectangles with dimensions 18  2, 12  3 and 6  6 by cutting and rearranging as below:




similarly, from a sheet with dimensions 9  8 , we can make rectangles with dimensions 18  4 and 12  6 .

for a pair w and h, let f(w,h) be the number of distinct rectangles that can be made from a sheet with dimensions w h .
for example, f(2,1) = 0, f(2,2) = 1, f(9,4) = 3 and f(9,8) = 2. 
note that rectangles congruent to the initial one are not counted in f(w,h).
note also that rectangles with dimensions w h and dimensions h w are not considered distinct.

for an integer n, let g(n) be the sum of f(w,h) for all pairs w and h which satisfy 0 h w n.
we can verify that g(10) = 55, g(103) = 971745 and g(105) = 9992617687.

find g(1012). give your answer modulo 108.
"""