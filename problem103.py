"""
Let s(a) represent the sum of elements in set a of size n. we shall call it a special sum set if for any two non-empty disjoint subsets, b and c, the following properties are true:
s(b)  s(c); that is, sums of subsets cannot be equal.
if b contains more elements than c then s(b)  s(c).
if s(a) is minimised for a given n, we shall call it an optimum special sum set. the first five optimum special sum sets are given below.
n = 1: {1}n = 2: {1, 2}n = 3: {2, 3, 4}n = 4: {3, 5, 6, 7}n = 5: {6, 9, 11, 12, 13}
it seems that for a given optimum set, a = {a1, a2, ... , an}, the next optimum set is of the form b = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.
by applying this "rule" we would expect the optimum set for n = 6 to be a = {11, 17, 20, 22, 23, 24}, with s(a) = 117. however, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. the optimum set for n = 6 is a = {11, 18, 19, 20, 22, 25}, with s(a) = 115 and corresponding set string: 111819202225.
given that a is an optimum special sum set for n = 7, find its set string.
note: this problem is related to problems 105 and 106.
"""