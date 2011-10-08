"""
The following game is a classic example of combinatorial game theory:

two players start with a strip of n white squares and they take alternate turns.
on each turn, a player picks two contiguous white squares and paints them black.
the first player who cannot make a move loses.

if n = 1, there are no valid moves, so the first player loses automatically.
if n = 2, there is only one valid move, after which the second player loses.
if n = 3, there are two valid moves, but both leave a situation where the second player loses.
if n = 4, there are three valid moves for the first player; she can win the game by painting the two middle squares.
if n = 5, there are four valid moves for the first player (shown below in red); but no matter what she does, the second player (blue) wins.



so, for 1 n  5, there are 3 values of n for which the first player can force a win.
similarly, for 1 n  50, there are 40 values of n for which the first player can force a win.

for 1 n  1 000 000, how many values of n are there for which the first player can force a win?
"""