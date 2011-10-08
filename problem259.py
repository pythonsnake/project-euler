"""
A positive integer will be called reachable if it can result from an arithmetic expression obeying the following rules:

uses the digits 1 through 9, in that order and exactly once each.
any successive digits can be concatenated (for example, using the digits 2, 3 and 4 we obtain the number 234).
only the four usual binary arithmetic operations (addition, subtraction, multiplication and division) are allowed.
each operation can be used any number of times, or not at all.
unary minus is not allowed.
any number of (possibly nested) parentheses may be used to define the order of operations.
for example, 42 is reachable, since (1/23) * ((4*5)-6) * (78-9) = 42.

what is the sum of all positive reachable integers?
"""