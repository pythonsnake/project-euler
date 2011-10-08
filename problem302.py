"""
A positive integer n is powerful if p2 is a divisor of n for every prime factor p in n.


a positive integer n is a perfect power if n can be expressed as a power of another positive integer.


a positive integer n is an achilles number if n is powerful but not a perfect power. for example, 864 and 1800 are achilles numbers: 864 = 25·33 and 1800 = 23·32·52.


we shall call a positive integer s a strong achilles number if both s and φ(s) are achilles numbers.1
for example, 864 is a strong achilles number: φ(864) = 288 = 25·32. however, 1800 isn't a strong achilles number because: φ(1800) = 480 = 25·31·51.

there are 7 strong achilles numbers below 104 and 656 below 108.


how many strong achilles numbers are there below 1018?


1 φ denotes euler's totient function.
"""