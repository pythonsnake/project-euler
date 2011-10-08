"""
Tatami are rectangular mats, used to completely cover the floor of a room, without overlap.

assuming that the only type of available tatami has dimensions 12, there are obviously some limitations for the shape and size of the rooms that can be covered.

for this problem, we consider only rectangular rooms with integer dimensions a, b and even size s = a·b.
we use the term 'size' to denote the floor surface area of the room, and — without loss of generality — we add the condition a b.

there is one rule to follow when laying out tatami: there must be no points where corners of four different mats meet.
for example, consider the two arrangements below for a 44 room:



the arrangement on the left is acceptable, whereas the one on the right is not: a red "x" in the middle, marks the point where four tatami meet.

because of this rule, certain even-sized rooms cannot be covered with tatami: we call them tatami-free rooms.
further, we define t(s) as the number of tatami-free rooms of size s.

the smallest tatami-free room has size s = 70 and dimensions 710.
all the other rooms of size s = 70 can be covered with tatami; they are: 170, 235 and 514.
hence, t(70) = 1.

similarly, we can verify that t(1320) = 5 because there are exactly 5 tatami-free rooms of size s = 1320:
2066, 2260, 2455, 3044 and 3340.
in fact, s = 1320 is the smallest room-size s for which t(s) = 5.

find the smallest room-size s for which t(s) = 200.
"""