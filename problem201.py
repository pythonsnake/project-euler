"""
For any set a of numbers, let sum(a) be the sum of the elements of a.
consider the set b = {1,3,6,8,10,11}. there are 20 subsets of b containing three elements, and their sums are:


sum({1,3,6}) = 10,
sum({1,3,8}) = 12,
sum({1,3,10}) = 14,
sum({1,3,11}) = 15,
sum({1,6,8}) = 15,
sum({1,6,10}) = 17,
sum({1,6,11}) = 18,
sum({1,8,10}) = 19,
sum({1,8,11}) = 20,
sum({1,10,11}) = 22,
sum({3,6,8}) = 17,
sum({3,6,10}) = 19,
sum({3,6,11}) = 20,
sum({3,8,10}) = 21,
sum({3,8,11}) = 22,
sum({3,10,11}) = 24,
sum({6,8,10}) = 24,
sum({6,8,11}) = 25,
sum({6,10,11}) = 27,
sum({8,10,11}) = 29.

some of these sums occur more than once, others are unique.
for a set a, let u(a,k) be the set of unique sums of k-element subsets of a, in our example we find u(b,3) = {10,12,14,18,21,25,27,29} and sum(u(b,3)) = 156.

now consider the 100-element set s = {12, 22, ... , 1002}.
s has 100891344545564193334812497256 50-element subsets.

determine the sum of all integers which are the sum of exactly one of the 50-element subsets of s, i.e. find sum(u(s,50)).
"""