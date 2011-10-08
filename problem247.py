"""
Consider the region constrained by 1 x and 0 y 1/x.

let s1 be the largest square that can fit under the curve.
let s2 be the largest square that fits in the remaining area, and so on. 
let the index of sn be the pair (left, below) indicating the number of squares to the left of sn and the number of squares below sn.




the diagram shows some such squares labelled by number. 
s2 has one square to its left and none below, so the index of s2 is (1,0).
it can be seen that the index of s32 is (1,1) as is the index of s50. 
50 is the largest n for which the index of sn is (1,1).


what is the largest n for which the index of sn is (3,3)?
"""