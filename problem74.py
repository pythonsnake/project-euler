"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145
perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
169  363601  1454  169
871  45361  871
872  45362  872
it is not difficult to prove that every starting number will eventually get stuck in a loop. for example,
69  363600  1454  169  363601 ( 1454)
78  45360  871  45361 ( 871)
540  145 ( 145)
starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
how many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""