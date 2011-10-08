"""
A modified collatz sequence of integers is obtained from a starting value a1 in the following way:

an+1 = an/3 if an is divisible by 3. we shall denote this as a large downward step, "d".

an+1 = (4an + 2)/3 if an divided by 3 gives a remainder of 1. we shall denote this as an upward step, "u".


an+1 = (2an - 1)/3 if an divided by 3 gives a remainder of 2. we shall denote this as a small downward step, "d".




the sequence terminates when some an = 1.


given any integer, we can list out the sequence of steps.
for instance if a1=231, then the sequence {an}={231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps "ddddduuddd".


of course, there are other sequences that begin with that same sequence "ddddduuddd....".
for instance, if a1=1004064, then the sequence is ddddduuddddduduuuddduuddduddd.
in fact, 1004064 is the smallest possible a1 106 that begins with the sequence ddddduuddd.


what is the smallest a1 1015 that begins with the sequence "uddduddddduddddddddddduddduudd"?
"""