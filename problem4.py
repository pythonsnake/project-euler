#-*-coding:utf-8 -*
"""
Problem 4 - Project Euler

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def isPalindromic(number):
    number=str(number)
    return number==number[::-1]

results=[]
for x in range(100*100, 999*999):
        if isPalindromic(x) is True:
            results.append(x)
print max(results)
#Solved
