"""
Whenever peter feels bored, he places some bowls, containing one bean each, in a circle. after this, he takes all the beans out of a certain bowl and drops them one by one in the bowls going clockwise. he repeats this, starting from the bowl he dropped the last bean in, until the initial situation appears again. for example with 5 bowls he acts as follows:



so with 5 bowls it takes peter 15 moves to return to the initial situation.

let m(x) represent the number of moves required to return to the initial situation, starting with x bowls. thus, m(5) = 15. it can also be verified that m(100) = 10920.

find m(2k+1). give your answer modulo 79.
"""