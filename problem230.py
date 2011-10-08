"""
For any two strings of digits, a and b, we define fa,b to be the sequence (a,b,ab,bab,abbab,...) in which each term is the concatenation of the previous two.

further, we define da,b(n) to be the nth digit in the first term of fa,b that contains at least n digits.

example:

let a=1415926535, b=8979323846. we wish to find da,b(35), say.

the first few terms of fa,b are:
1415926535
8979323846
14159265358979323846
897932384614159265358979323846
14159265358979323846897932384614159265358979323846

then da,b(35) is the 35th digit in the fifth term, which is 9.

now we use for a the first 100 digits of π behind the decimal point:
14159265358979323846264338327950288419716939937510 
58209749445923078164062862089986280348253421170679 

and for b the next hundred digits:

82148086513282306647093844609550582231725359408128 
48111745028410270193852110555964462294895493038196 .

find n = 0,1,...,17   10n da,b((127+19n)7n) .
"""