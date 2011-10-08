"""
Let c(x,y) be a circle passing through the points (x, y), (x, y+1), (x+1, y) and (x+1, y+1).

for positive integers m and n, let e(m,n) be a configuration which consists of the m·n circles:
{ c(x,y): 0 ≤ x m, 0 ≤ y n, x and y are integers }

an eulerian cycle on e(m,n) is a closed path that passes through each arc exactly once.
many such paths are possible on e(m,n), but we are only interested in those which are not self-crossing: 
a non-crossing path just touches itself at lattice points, but it never crosses itself.

the image below shows e(3,3) and an example of an eulerian non-crossing path.

let l(m,n) be the number of eulerian non-crossing paths on e(m,n).
for example, l(1,2) = 2, l(2,2) = 37 and l(3,3) = 104290.

find l(6,10) mod 1010.
"""