"""
All positive integers can be partitioned in such a way that each and every term of the partition can be expressed as 2ix3j, where i,j  0.

let's consider only those such partitions where none of the terms can divide any of the other terms.
for example, the partition of 17 = 2 + 6 + 9 = (21x30 + 21x31 + 20x32) would not be valid since 2 can divide 6. neither would the partition 17 = 16 + 1 = (24x30 + 20x30) since 1 can divide 16. the only valid partition of 17 would be 8 + 9 = (23x30 + 20x32).

many integers have more than one valid partition, the first being 11 having the following two partitions.
11 = 2 + 9 = (21x30 + 20x32)
11 = 8 + 3 = (23x30 + 20x31)

let's define p(n) as the number of valid partitions of n. for example, p(11) = 2.

let's consider only the prime integers q which would have a single valid partition such as p(17).

the sum of the primes q 100 such that p(q)=1 equals 233.

find the sum of the primes q 1000000 such that p(q)=1.
"""