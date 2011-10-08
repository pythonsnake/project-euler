"""
A game is played with three piles of stones and two players.
at her turn, a player removes one or more stones from the piles. however, if she takes stones from more than one pile, she must remove the same number of stones from each of the selected piles.

in other words, the player chooses some n>0 and removes:
n stones from any single pile; or
n stones from each of any two piles (2n total); or
n stones from each of the three piles (3n total).
the player taking the last stone(s) wins the game.

a winning configuration is one where the first player can force a win.
for example, (0,0,13), (0,11,11) and (5,5,5) are winning configurations because the first player can immediately remove all stones.

a losing configuration is one where the second player can force a win, no matter what the first player does. 
for example, (0,1,2) and (1,3,3) are losing configurations: any legal move leaves a winning configuration for the second player.

consider all  losing configurations (xi,yi,zi) where xi yi zi 100.
we can verify that σ(xi+yi+zi) = 173895 for these.

find σ(xi+yi+zi) where (xi,yi,zi) ranges over the losing configurations
with xi yi zi 1000.
"""