"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
not all numbers produce palindromes so quickly. for example,
349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337
that is, 349 took three iterations to arrive at a palindrome.
although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. a number that never forms a palindrome through the reverse and add process is called a lychrel number. due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is lychrel until proven otherwise. in addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. in fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
surprisingly, there are palindromic numbers that are themselves lychrel numbers; the first example is 4994.
how many lychrel numbers are there below ten-thousand?
note: wording was modified slightly on 24 april 2007 to emphasise the theoretical nature of lychrel numbers.
"""