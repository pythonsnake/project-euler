"""
An infinite sequence of real numbers a(n) is defined for all integers n as follows:


for example,a(0) = 
    11!
    +
    12!
    +
    13!
    + ... = e  1 
a(1) = 
    e  11!
    +
    12!
    +
    13!
    + ... = 2e  3 
a(2) = 
    2e  31!
    +
    e  12!
    +
    13!
    + ... =
    72
    e  6 

with e = 2.7182818... being euler's constant.


it can be shown that a(n) is of the form 
    
    a(n) e + b(n)n!
    for integers a(n) and b(n). 
    
for example a(10) = 
    
    328161643 e  65269448610!
    .

find a(109) + b(109) and give your answer mod 77 777 777.
"""