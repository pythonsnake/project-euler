"""
In the game of darts a player throws three darts at a target board which is split into twenty equal sized sections numbered one to twenty.


the score of a dart is determined by the number of the region that the dart lands in. a dart landing outside the red/green outer ring scores zero. the black and cream regions inside this ring represent single scores. however, the red/green outer ring and middle ring score double and treble scores respectively.
at the centre of the board are two concentric circles called the bull region, or bulls-eye. the outer bull is worth 25 points and the inner bull is a double, worth 50 points.
there are many variations of rules but in the most popular game the players will begin with a score 301 or 501 and the first player to reduce their running total to zero is a winner. however, it is normal to play a "doubles out" system, which means that the player must land a double (including the double bulls-eye at the centre of the board) on their final dart to win; any other dart that would reduce their running total to one or lower means the score for that set of three darts is "bust".
when a player is able to finish  on their current score it is called a "checkout" and the highest checkout is 170: t20 t20 d25 (two treble 20s and double bull).
there are exactly eleven distinct ways to checkout on a score of 6:

d3
 
 
d1
d2
 
s2
d2
 
d2
d1
 
s4
d1
 
s1
s1
d2
s1
t1
d1
s1
s3
d1
d1
d1
d1
d1
s2
d1
s2
s2
d1

note that d1 d2 is considered different to d2 d1 as they finish on different doubles. however, the combination s1 t1 d1 is considered the same as t1 s1 d1.
in addition we shall not include misses in considering combinations; for example, d3 is the same as 0 d3 and 0 0 d3.
incredibly there are 42336 distinct ways of checking out in total.
how many distinct ways can a player checkout with a score less than 100?
"""