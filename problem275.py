"""
Let us define a balanced sculpture of order n as follows:
a polyomino made up of n+1 tiles known as the blocks (n tiles) and the plinth (remaining tile);
the plinth has its centre at position (x = 0, y = 0);
the blocks have y-coordinates greater than zero (so the plinth is the unique lowest tile);
the centre of mass of all the blocks, combined, has x-coordinate equal to zero.
when counting the sculptures, any arrangements which are simply reflections about the y-axis, are not counted as distinct. for example, the 18 balanced sculptures of order 6 are shown below; note that each pair of mirror images (about the y-axis) is counted as one sculpture:


there are 964 balanced sculptures of order 10 and 360505 of order 15.how many balanced sculptures are there of order 18?
"""