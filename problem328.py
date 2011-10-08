"""
We are trying to find a hidden number selected from the set of integers {1, 2, ..., n} by asking questions. 
each number (question) we ask, has a cost equal to the number asked and we get one of three possible answers: "your guess is lower than the hidden number", or
 "yes, that's it!", or
 "your guess is higher than the hidden number".
given the value of n, an optimal strategy minimizes the total cost (i.e. the sum of all the questions asked) for the worst possible case. e.g.

if n=3, the best we can do is obviously to ask the number "2". the answer will immediately lead us to find the hidden number (at a total cost = 2).

if n=8, we might decide to use a "binary search" type of strategy: our first question would be "4" and if the hidden number is higher than 4 we will need one or two additional questions.
let our second question be "6". if the hidden number is still higher than 6, we will need a third question in order to discriminate between 7 and 8.
thus, our third question will be "7" and the total cost for this worst-case scenario will be 4+6+7=17.

we can improve considerably the worst-case cost for n=8, by asking "5" as our first question.
if we are told that the hidden number is higher than 5, our second question will be "7", then we'll know for certain what the hidden number is (for a total cost of 5+7=12).
if we are told that the hidden number is lower than 5, our second question will be "3" and if the hidden number is lower than 3 our third question will be "1", giving a total cost of 5+3+1=9.
since 12>9, the worst-case cost for this strategy is 12. that's better than what we achieved previously with the "binary search" strategy; it is also better than or equal to any other strategy.
so, in fact, we have just described an optimal strategy for n=8.

let c(n) be the worst-case cost achieved by an optimal strategy for n, as described above.
thus c(1) = 0, c(2) = 1, c(3) = 2 and c(8) = 12.
similarly, c(100) = 400 and c(n) = 17575.

find c(n).
"""