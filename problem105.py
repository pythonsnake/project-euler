"""
Let s(a) represent the sum of elements in set a of size n. we shall call it a special sum set if for any two non-empty disjoint subsets, b and c, the following properties are true:
s(b)  s(c); that is, sums of subsets cannot be equal.
if b contains more elements than c then s(b)  s(c).
for example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and s(a) = 1286.
using sets.txt (right click and "save link/target as..."), a 4k text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, a1, a2, ..., ak, and find the value of s(a1) + s(a2) + ... + s(ak).
note: this problem is related to problems 103 and 106.
"""