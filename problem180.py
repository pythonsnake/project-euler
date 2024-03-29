"""
For any integer n, consider the three functions
f1,n(x,y,z) = xn+1 + yn+1zn+1f2,n(x,y,z) = (xy + yz + zx)*(xn-1 + yn-1zn-1)f3,n(x,y,z) = xyz*(xn-2 + yn-2zn-2)
and their combination
fn(x,y,z) = f1,n(x,y,z) + f2,n(x,y,z) f3,n(x,y,z)
we call (x,y,z) a golden triple of order k if x, y, and z are all rational numbers of the form a / b with
0 a b k and there is (at least) one integer n, so that fn(x,y,z) = 0.
let s(x,y,z) = x + y + z.
let t = u / v be the sum of all distinct s(x,y,z) for all golden triples (x,y,z) of order 35. all the s(x,y,z) and t  must be in reduced form.
find u + v.
"""