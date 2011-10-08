"""
The rsa encryption is based on the following procedure:
generate two distinct primes p and q.compute n=pq and φ=(p-1)(q-1).
find an integer e, 1eφ, such that gcd(e,φ)=1.
a message in this system is a number in the interval [0,n-1].
a text to be encrypted is then somehow converted to messages (numbers in the interval [0,n-1]).
to encrypt the text,  for each message, m, c=me mod n is calculated.
to decrypt the text, the following procedure is needed: calculate d such that ed=1 mod φ, then for each encrypted message, c, calculate m=cd mod n.
there exist values of e and m  such that me mod n=m.we call messages m for which me mod n=m unconcealed messages.
an issue when choosing e is that there should not be too many unconcealed messages.  for instance, let p=19 and q=37.
then n=19*37=703 and φ=18*36=648.
if we choose e=181, then, although gcd(181,648)=1 it turns out that all possible messagesm (0mn-1) are unconcealed when calculating me mod n.
for any valid choice of e there exist some unconcealed messages.
it's important that the number of unconcealed messages is at a minimum.
choose p=1009 and q=3643.
find the sum of all values of e, 1eφ(1009,3643) and gcd(e,φ)=1, so that the number of unconcealed messages for this value of e is at a minimum.
"""