"""
Let p = p1 p2 p3 ... be an infinite sequence of random digits, selected from {0,1,2,3,4,5,6,7,8,9} with equal probability.
it can be seen that p corresponds to the real number 0.p1 p2 p3 .... 
it can also be seen that choosing a random real number from the interval [0,1) is equivalent to choosing an infinite sequence of random digits selected from {0,1,2,3,4,5,6,7,8,9} with equal probability.

for any positive integer n with d decimal digits, let k be the smallest index such that pk, pk+1, ...pk+d-1 are the decimal digits of n, in the same order.
also, let g(n) be the expected value of k; it can be proven that g(n) is always finite and, interestingly, always an integer number.

for example, if n = 535, then
for p = 31415926535897...., we get k = 9
for p = 355287143650049560000490848764084685354..., we get k = 36
etc and we find that g(535) = 1008.

given that , find 

note:  represents the floor function.
"""