"""
Table.p298, table.p298 th, table.p298 td {
  border-width: 1px 1px 1px 1px;
  border-style: solid solid solid solid;
  border-color: black black black black;
  text-align:center;
  -moz-border-radius: 0px 0px 0px 0px;
}
table.p298 {
  border-spacing: 1px;
  border-collapse: separate;
  background-color: rgb(255,255,255);
}
table.p298 th, table.p298 td {
  padding: 1px 6px 1px 6px;
}
table.p298 th { background-color: rgb(200,220,250); }
table.p298 td { background-color: rgb(255,255,255); }
larry and robin play a memory game involving of a sequence of random numbers between 1 and 10, inclusive, that are called out one at a time. each player can remember up to 5 previous numbers. when the called number is in a player's memory, that player is awarded a point. if it's not, the player adds the called number to his memory, removing another number if his memory is full.

both players start with empty memories. both players always add new missed numbers to their memory but use a different strategy in deciding which number to remove:
larry's strategy is to remove the number that hasn't been called in the longest time.
robin's strategy is to remove the number that's been in the memory the longest time.

example game:turn
  callednumber
  larry'smemory
  larry'sscore
  robin'smemory
  robin'sscore
1
  1
  1
  0
  1
  0
2
  2
  1,2
  0
  1,2
  0
3
  4
  1,2,4
  0
  1,2,4
  0
4
  6
  1,2,4,6
  0
  1,2,4,6
  0
5
  1
  1,2,4,6
  1
  1,2,4,6
  1
6
  8
  1,2,4,6,8
  1
  1,2,4,6,8
  1
7
  10
  1,4,6,8,10
  1
  2,4,6,8,10
  1
8
  2
  1,2,6,8,10
  1
  2,4,6,8,10
  2
9
  4
  1,2,4,8,10
  1
  2,4,6,8,10
  3
10
  1
  1,2,4,8,10
  2
  1,4,6,8,10
  3


denoting larry's score by l and robin's score by r, what is the expected value of |l-r| after 50 turns? give your answer rounded to eight decimal places using the format x.xxxxxxxx .
"""