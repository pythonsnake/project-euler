"""
- a sierpiński graph of order-1 (s1) is an equilateral triangle.
- sn+1 is obtained from sn by positioning three copies of sn so that every pair of copies has one common corner.




let c(n) be the number of cycles that pass exactly once through all the vertices of sn.
for example, c(3) = 8 because eight such cycles can be drawn on s3, as shown below:




it can also be verified that :
c(1) = c(2) = 1
c(5) = 71328803586048
c(10 000) mod 108 = 37652224
c(10 000) mod 138 = 617720485

find c(c(c(10 000))) mod 138.
"""