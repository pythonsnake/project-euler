"""
In the game, monopoly, the standard board is set up in the following way:

go
a1
cc1
a2
t1
r1
b1
ch1
b2
b3
jail
h2
 
c1
t2
 
u1
h1
 
c2
ch3
 
c3
r4
 
r2
g3
 
d1
cc3
 
cc2
g2
 
d2
g1
 
d3
g2j
f3
u2
f2
f1
r3
e3
e2
ch2
e1
fp

a player starts on the go square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. without any further rules we would expect to visit each square with equal probability: 2.5%. however, landing on g2j (go to jail), cc (community chest), and ch (chance) changes this distribution.
in addition to g2j, and one card from each of cc and ch, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. instead they proceed directly to jail.
at the beginning of the game, the cc and ch cards are shuffled. when a player lands on cc or ch they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. there are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the cc/ch square.
community chest (2/16 cards):
advance to go
go to jail

chance (10/16 cards):
advance to go
go to jail
go to c1
go to e3
go to h2
go to r1
go to next r (railway company)
go to next r
go to next u (utility company)
go back 3 squares.

the heart of this problem concerns the likelihood of visiting a particular square. that is, the probability of finishing at that square after a roll. for this reason it should be clear that, with the exception of g2j for which the probability of finishing on it is zero, the ch squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. we shall make no distinction between "just visiting" and being sent to jail, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.
by starting at go and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.
statistically it can be shown that the three most popular squares, in order, are jail (6.24%) = square 10, e3 (3.18%) = square 24, and go (3.09%) = square 00. so these three most popular squares can be listed with the six-digit modal string: 102400.
if, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""