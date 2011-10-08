"""
For any prime p the number n(p,q) is defined by
n(p,q) = n=0 to q tn*pn with tn generated by the following random number generator:

s0 = 290797
sn+1 = sn2 mod 50515093
tn = sn mod p


let nfac(p,q) be the factorial of n(p,q).
let nf(p,q) be the number of factors p in nfac(p,q).


you are given that nf(3,10000) mod 320=624955285.


find nf(61,107) mod 6110
"""