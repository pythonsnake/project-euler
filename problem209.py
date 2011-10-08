"""
A k-input binary truth table is a map from k input bits
(binary digits, 0 [false] or 1 [true]) to 1 output bit. for example, the 2-input binary truth tables for the logical and and xor functions are:

x
y
x and y000010100111x
y
x xor y000011101110how many 6-input binary truth tables, τ, satisfy the formula

τ(a, b, c, d, e, f) and τ(b, c, d, e, f, a xor (b and c)) = 0
for all 6-bit inputs (a, b, c, d, e, f)?
"""