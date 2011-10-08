"""
The radical of n, rad(n), is the product of distinct prime factors of n. for example, 504 = 23 32 7, so rad(504) = 2  3  7 = 42.
if we calculate rad(n) for 1 n  10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:
unsorted
 
sorted
n
rad(n)

n
rad(n)
k
11
 
111
22
 
222
33
 
423
42
 
824
55
 
335
66
 
936
77
 
557
82
 
668
93
 
779
1010
 
101010
let e(k) be the kth element in the sorted n column; for example, e(4) = 8 and e(6) = 9.
if rad(n) is sorted for 1 n  100000, find e(10000).
"""