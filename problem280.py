"""
A laborious ant walks randomly on a 5x5 grid. the walk starts from the central square. at each step, the ant moves to an adjacent square at random, without leaving the grid; thus there are 2, 3 or 4 possible moves at each step depending on the ant's position.

at the start of the walk, a seed is placed on each square of the lower row. when the ant isn't carrying a seed and reaches a square of the lower row containing a seed, it will start to carry the seed. the ant will drop the seed on the first empty square of the upper row it eventually reaches.

what's the expected number of steps until all seeds have been dropped in the top row? 
give your answer rounded to 6 decimal places.
"""