"""
Define f(0)=1 and f(n) to be the number of ways to write n as a sum of powers of 2 where no power occurs more than twice. 

for example, f(10)=5 since there are five different ways to express 10:10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1

it can be shown that for every fraction p/q (p0, q0) there exists at least one integer n such that f(n)/f(n-1)=p/q.
for instance, the smallest n for which f(n)/f(n-1)=13/17 is 241.
the binary expansion of 241 is 11110001.
reading this binary number from the most significant bit to the least significant bit there are 4 one's, 3 zeroes and 1 one. we shall call the string 4,3,1 the shortened binary expansion of 241.
find the shortened binary expansion of the smallest n for which f(n)/f(n-1)=123456789/987654321.
give your answer as comma separated integers, without any whitespaces.
"""