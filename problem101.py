"""
If we are presented with the first k terms of a sequence it is impossible to say with certainty the value of the next term, as there are infinitely many polynomial functions that can model the sequence.
as an example, let us consider the sequence of cube numbers. this is defined by the generating function, un = n3: 1, 8, 27, 64, 125, 216, ...
suppose we were only given the first two terms of this sequence. working on the principle that "simple is best" we should assume a linear relationship and predict the next term to be 15 (common difference 7). even if we were presented with the first three terms, by the same principle of simplicity, a quadratic relationship should be assumed.
we shall define op(k, n) to be the nth term of the optimum polynomial generating function for the first k terms of a sequence. it should be clear that op(k, n) will accurately generate the terms of the sequence for n k, and potentially the first incorrect term (fit) will be op(k, k+1); in which case we shall call it a bad op (bop).
as a basis, if we were only given the first term of sequence, it would be most sensible to assume constancy; that is, for n  2, op(1, n) = u1.
hence we obtain the following ops for the cubic sequence:

op(1, n) = 1
1, 1, 1, 1, ...
op(2, n) = 7n6
1, 8, 15, ...
op(3, n) = 6n211n+6     
1, 8, 27, 58, ...
op(4, n) = n3
1, 8, 27, 64, 125, ...

clearly no bops exist for k  4.
by considering the sum of fits generated by the bops (indicated in red above), we obtain 1 + 15 + 58 = 74.
consider the following tenth degree polynomial generating function:
un = 1 n + n2n3 + n4n5 + n6n7 + n8n9 + n10
find the sum of fits for the bops.
"""