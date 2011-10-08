"""
One variant of n.g. de bruijn's silver dollar game can be described as follows:

on a strip of squares a number of coins are placed, at most one coin per square. only one coin, called the silver dollar, has any value. two players take turns making moves. at each turn a player must make either a regular or a special move.

a regular move consists of selecting one coin and moving it one or more squares to the left. the coin cannot move out of the strip or jump on or over another coin.

alternatively, the player can choose to make the special move of pocketing the leftmost coin rather than making a regular move. if no regular moves are possible, the player is forced to pocket the leftmost coin.

the winner is the player who pockets the silver dollar.





a winning configuration is an arrangement of coins on the strip where the first player can force a win no matter what the second player does.

let w(n,c) be the number of winning configurations for a strip of n squares, c worthless coins and one silver dollar.

you are given that w(10,2) = 324 and w(100,10) = 1514704946113500.

find w(1 000 000, 100) modulo the semiprime 1000 036 000 099 (= 1 000 003 · 1 000 033).
"""