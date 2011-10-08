"""
For any positive integer n the function next_prime(n) returns the smallest prime p  such that pn.


the sequence a(n) is defined by:
a(1)=next_prime(1014) and a(n)=next_prime(a(n-1)) for n1.


the fibonacci sequence f(n) is defined by:
f(0)=0, f(1)=1 and f(n)=f(n-1)+f(n-2) for n1.


the sequence b(n) is defined as f(a(n)).


find b(n) for 1n100 000. 
give your answer mod 1234567891011.
"""