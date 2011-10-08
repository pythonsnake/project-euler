"""
Let x1, x2,..., xn be a sequence of length n such that:
x1 = 2
for all 1 i n : xi-1xi
for all i and j with 1 i, j n : (xi) j  (xj + 1)i

there are only five such sequences of length 2, namely:
{2,4}, {2,5}, {2,6}, {2,7} and {2,8}.
there are 293 such sequences of length 5; three examples are given below:
{2,5,11,25,55}, {2,6,14,36,88}, {2,8,22,64,181}.


let t(n) denote the number of such sequences of length n.
you are given that t(10) = 86195 and t(20) = 5227991891.


find t(1010) and give your answer modulo 109.
"""