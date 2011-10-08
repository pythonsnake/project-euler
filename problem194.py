"""
Consider graphs built with the units a: 
and b: , where the units are glued along
the vertical edges as in the graph .

a configuration of type (a,b,c) is a graph thus built of a units a and b units b, where the graph's vertices are coloured using up to c colours, so that no two adjacent vertices have the same colour.
the compound graph above is an example of a configuration of type (2,2,6), in fact of type (2,2,c) for all c  4.

let n(a,b,c) be the number of configurations of type (a,b,c).
for example, n(1,0,3) = 24, n(0,2,4) = 92928 and n(2,2,3) = 20736.

find the last 8 digits of n(25,75,1984).
"""