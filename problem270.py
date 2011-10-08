"""
A square piece of paper with integer dimensions nn is placed with a corner at the origin and two of its sides along the x- and y-axes. then, we cut it up respecting the following rules:
we only make straight cuts between two points lying on different sides of the square, and having integer coordinates.
two cuts cannot cross, but several cuts can meet at the same border point.
proceed until no more legal cuts can be made.
counting any reflections or rotations as distinct, we call c(n) the number of ways to cut an nn square. for example, c(1) = 2 and c(2) = 30 (shown below).


what is c(30) mod 108 ?
"""