"""
A train is used to transport four carriages in the order: abcd. however, sometimes when the train arrives to collect the carriages they are not in the correct order. 
to rearrange the carriages they are all shunted on to a large rotating turntable. after the carriages are uncoupled at a specific point the train moves off the turntable pulling the carriages still attached with it. the remaining carriages are rotated 180 degrees. all of the carriages are then rejoined and this process is repeated as often as necessary in order to obtain the least number of uses of the turntable.
some arrangements, such as adcb, can be solved easily: the carriages are separated between a and d, and after dcb are rotated the correct order has been achieved.

however, simple simon, the train driver, is not known for his efficiency, so he always solves the problem by initially getting carriage a in the correct place, then carriage b, and so on.

using four carriages, the worst possible arrangements for simon, which we shall call maximix arrangements, are dacb and dbac; each requiring him five rotations (although, using the most efficient approach, they could be solved using just three rotations). the process he uses for dacb is shown below.




it can be verified that there are 24 maximix arrangements for six carriages, of which the tenth lexicographic maximix arrangement is dfaecb.

find the 2011th lexicographic maximix arrangement for eleven carriages.
"""