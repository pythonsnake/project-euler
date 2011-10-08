"""
We define the rounded-square-root of a positive integer n as the square root of n rounded to the nearest integer.

the following procedure (essentially heron's method adapted to integer arithmetic) finds the rounded-square-root of n:
let d be the number of digits of the number n.
if d is odd, set x0 = 210(d-1)⁄2.
if d is even, set x0 = 710(d-2)⁄2.
repeat:




until xk+1 = xk.

as an example, let us find the rounded-square-root of n = 4321.n has 4 digits, so x0 = 710(4-2)⁄2 = 70.
since x2 = x1, we stop here.
so, after just two iterations, we have found that the rounded-square-root of 4321 is 66 (the actual square root is 65.7343137…).

the number of iterations required when using this method is surprisingly low.
for example, we can find the rounded-square-root of a 5-digit integer (10,000 n  99,999) with an average of 3.2102888889 iterations (the average value was rounded to 10 decimal places).

using the procedure described above, what is the average number of iterations required to find the rounded-square-root of a 14-digit number (1013n  1014)?
give your answer rounded to 10 decimal places.

note: the symbols x and x represent the floor function and ceiling function respectively.
"""