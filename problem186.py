"""
Here are the records from a busy telephone system with one million users:

recnrcallercalled120000710005326001835004393600863701497.........
the telephone number of the caller and the called number in record n are caller(n) = s2n-1 and called(n) = s2n where s1,2,3,... come from the "lagged fibonacci generator":

for 1  k  55, sk = [100003 - 200003k + 300007k3] (modulo 1000000)
for 56  k, sk = [sk-24 + sk-55] (modulo 1000000)

if caller(n) = called(n) then the user is assumed to have misdialled and the call fails; otherwise the call is successful.

from the start of the records, we say that any pair of users x and y are friends if x calls y or vice-versa. similarly, x is a friend of a friend of z if x is a friend of y and y is a friend of z; and so on for longer chains.

the prime minister's phone number is 524287. after how many successful calls, not counting misdials, will 99% of the users (including the pm) be a friend, or a friend of a friend etc., of the prime minister?
"""