"""
A game is played with two piles of stones and two players. at her turn, a player removes a number of stones from the larger pile. the number of stones she removes must be a positive multiple of the number of stones in the smaller pile.



e.g., let the ordered pair(6,14) describe a configuration with 6 stones in the smaller pile and 14 stones in the larger pile, then the first player can remove 6 or 12 stones from the larger pile.



the player taking all the stones from a pile wins the game.



a winning configuration is one where the first player can force a win. for example, (1,5), (2,6) and (3,12) are winning configurations because the first player can immediately remove all stones in the second pile.



a losing configuration is one where the second player can force a win, no matter what the first player does. for example, (2,3) and (3,4) are losing configurations: any legal move leaves a winning configuration for the second player.



define s(n) as the sum of (xi+yi) for all losing configurations (xi,yi), 0 xiyin. we can verify that s(10) = 211 and s(104) = 230312207313.



find s(1016) mod 710.
"""