"""
A small child has a “number caterpillar” consisting of forty jigsaw pieces, each with one number on it, which, when connected together in a line, reveal the numbers 1 to 40 in order.

every night, the child's father has to pick up the pieces of the caterpillar that have been scattered across the play room. he picks up the pieces at random and places them in the correct order. as the caterpillar is built up in this way, it forms distinct segments that gradually merge together. the number of segments starts at zero (no pieces placed), generally increases up to about eleven or twelve, then tends to drop again before finishing at a single segment (all pieces placed).

for example:

piece placed
segments so far121422936434554354……

let m be the maximum number of segments encountered during a random tidy-up of the caterpillar.
for a caterpillar of ten pieces, the number of possibilities for each m is

m
possibilities1512      2250912      31815264      41418112      5144000      

so the most likely value of m is 3 and the average value is 385643⁄113400 = 3.400732, rounded to six decimal places.

the most likely value of m for a forty-piece caterpillar is 11; but what is the average value of m?
give your answer rounded to six decimal places.
"""