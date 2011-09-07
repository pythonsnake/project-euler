#-*-coding:utf-8 -*
"""
Problem 4 - Project Euler

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def isPalindromic(number):
    number=str(number)
    a=number[0:len(number)/2]
    if len(number)%2==0 and a==number[len(number)/2:len(number)][::-1]:
        return True
    elif len(number)%2!=0 and a==number[len(number)/2+1:len(number)][::-1]:
        return True
    return False

#test
print "3456543 is palindromic ?", isPalindromic(3456543)
print "2442 is palindromic ?", isPalindromic(2442)
print "2343 is palindromic ?", isPalindromic(2343)

#Solved
