"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
high card: highest value card.
one pair: two cards of the same value.
two pairs: two different pairs.
three of a kind: three cards of the same value.
straight: all cards are consecutive values.
flush: all cards of the same suit.
full house: three of a kind and a pair.
four of a kind: four cards of the same value.
straight flush: all cards are consecutive values of same suit.
royal flush: ten, jack, queen, king, ace, in same suit.
the cards are valued in the order:2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace.
if two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). but if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
consider the following five hands dealt to two players:

hand player 1 player 2 winner
1 5h 5c 6s 7s kdpair of fives 2c 3s 8s 8d tdpair of eights player 2
2 5d 8c 9s js achighest card ace 2c 5c 7d 8s qhhighest card queen player 1
3 2d 9c as ah acthree aces 3d 6d 7d td qdflush  with diamonds player 2
4 4d 6s 9h qh qcpair of queenshighest card nine 3d 6d 7h qd qspair of queenshighest card seven player 1
5 2h 2d 4c 4d 4sfull housewith three fours 3c 3d 3s 9s 9dfull housewith three threes player 1

the file, poker.txt, contains one-thousand random hands dealt to two players. each line of the file contains ten cards (separated by a single space): the first five are player 1's cards and the last five are player 2's cards. you can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
how many hands does player 1 win?
"""