"""
Sam and max are asked to transform two digital clocks into two "digital root" clocks.
a digital root clock is a digital clock that calculates digital roots step by step.

when a clock is fed a number, it will show it and then it will start the calculation, showing all the intermediate values until it gets to the result.
for example, if the clock is fed the number 137, it will show: "137"  "11"  "2" and then it will go black, waiting for the next number.

every digital number consists of some light segments: three horizontal (top, middle, bottom) and four vertical (top-left, top-right, bottom-left, bottom-right).
number "1" is made of vertical top-right and bottom-right, number "4" is made by middle horizontal and vertical top-left, top-right and bottom-right. number "8" lights them all.

the clocks consume energy only when segments are turned on/off.
to turn on a "2" will cost 5 transitions, while a "7" will cost only 4 transitions.

sam and max built two different clocks.

sam's clock is fed e.g. number 137: the clock shows "137", then the panel is turned off, then the next number ("11") is turned on, then the panel is turned off again and finally the last number ("2") is turned on and, after some time, off.
for the example, with number 137, sam's clock requires:"137"
:
(2 + 5 + 4)  2 = 22 transitions ("137" on/off).
"11"
:
(2 + 2)  2 = 8 transitions ("11" on/off).
"2"
:
(5)  2 = 10 transitions ("2" on/off).

for a grand total of 40 transitions.

max's clock works differently. instead of turning off the whole panel, it is smart enough to turn off only those segments that won't be needed for the next number.
for number 137, max's clock requires:"137"
:
2 + 5 + 4 = 11 transitions ("137" on)
7 transitions (to turn off the segments that are not needed for number "11").
"11"
:
0 transitions (number "11" is already turned on correctly)
3 transitions (to turn off the first "1" and the bottom part of the second "1"; 
the top part is common with number "2").
"2"
:
4 tansitions (to turn on the remaining segments in order to get a "2")
5 transitions (to turn off number "2").

for a grand total of 30 transitions.

of course, max's clock consumes less power than sam's one.
the two clocks are fed all the prime numbers between a = 107 and b = 2107. 
find the difference between the total number of transitions needed by sam's clock and that needed by max's one.
"""