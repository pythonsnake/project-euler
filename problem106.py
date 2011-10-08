"""
Let s(a) represent the sum of elements in set a of size n. we shall call it a special sum set if for any two non-empty disjoint subsets, b and c, the following properties are true:
s(b)  s(c); that is, sums of subsets cannot be equal.
if b contains more elements than c then s(b)  s(c).
for this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.
surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.
for n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?
note: this problem is related to problems 103 and 105.
"""