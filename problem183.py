"""
Let n be a positive integer and let n be split into k equal parts, r = n/k, so that n = r + r + ... + r.
let p be the product of these parts, p = r r  ... r = rk.

for example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then p = 2.25 = 51.53632.

let m(n) = pmax for a given value of n.

it turns out that the maximum for n = 11 is found by splitting eleven into four equal parts which leads to pmax = (11/4)4; that is, m(11) = 14641/256 = 57.19140625, which is a terminating decimal.

however, for n = 8 the maximum is achieved by splitting it into three equal parts, so m(8) = 512/27, which is a non-terminating decimal.

let d(n) = n if m(n) is a non-terminating decimal and d(n) = -n if m(n) is a terminating decimal.

for example, σd(n) for 5  n  100 is 2438.

find σd(n) for 5  n  10000.
"""