"""
Let d0 be the two-letter string "fa".  for n1, derive dn from dn-1 by the string-rewriting rules:

"a"  "arbfr"
"b"  "lfalb"

thus, d0 = "fa", d1 = "farbfr", d2 = "farbfrrlfalbfr", and so on.

these strings can be interpreted as instructions to a computer graphics program, with "f" meaning "draw forward one unit", "l" meaning "turn left 90 degrees", "r" meaning "turn right 90 degrees", and "a" and "b" being ignored.  the initial position of the computer cursor is (0,0), pointing up towards (0,1).

then dn is an exotic drawing known as the heighway dragon of order n.  for example, d10 is shown below; counting each "f" as one step, the highlighted spot at (18,16) is the position reached after 500 steps.




what is the position of the cursor after 1012 steps in d50 ?
give your answer in the form x,y with no spaces.
"""