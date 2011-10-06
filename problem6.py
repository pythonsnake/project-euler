"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
result1, result2, y, s = 0, 0, 0, []

for i in range(101): s.append(i**2)
for r in s: result2+=r
for x in range(101): result1=result1+x

print result2-result1

#Solved
