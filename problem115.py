"""
Note: this is a more difficult version of problem 114.
a row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.
let the fill-count function, f(m, n), represent the number of ways that a row can be filled.
for example, f(3, 29) = 673135 and f(3, 30) = 1089155.
that is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.
in the same way, for m = 10, it can be verified that f(10, 56) = 880711 and f(10, 57) = 1148904, so n = 57 is the least value for which the fill-count function first exceeds one million.
for m = 50, find the least value of n for which the fill-count function first exceeds one million.
"""