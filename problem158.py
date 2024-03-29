"""
Taking three different letters from the 26 letters of the alphabet, character strings of length three can be formed.
examples are 'abc', 'hat' and 'zyx'.
when we study these three examples we see that for 'abc' two characters come lexicographically after its neighbour to the left. 
for 'hat' there is exactly one character that comes lexicographically after its neighbour to the left. for 'zyx' there are zero characters that come lexicographically after its neighbour to the left.
in all there are 10400 strings of length 3 for which exactly one character comes lexicographically after its neighbour to the left.
we now consider strings of n  26 different characters from the alphabet. 
for every n, p(n) is the number of strings of length n for which exactly one character comes lexicographically after its neighbour to the left. 
what is the maximum value of p(n)?
"""