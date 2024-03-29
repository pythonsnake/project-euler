"""
Su doku (japanese meaning number place) is the name given to a popular puzzle concept. its origin is unclear, but credit must be attributed to leonhard euler who invented a similar, and much more difficult, puzzle idea called latin squares. the objective of su doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. below is an example of a typical starting puzzle grid and its solution grid.


0 0 39 0 00 0 1
0 2 03 0 58 0 6
6 0 00 0 14 0 0
0 0 87 0 00 0 6
1 0 20 0 07 0 8
9 0 00 0 82 0 0
0 0 28 0 00 0 5
6 0 92 0 30 1 0
5 0 00 0 93 0 0



4 8 39 6 72 5 1
9 2 13 4 58 7 6
6 5 78 2 14 9 3
5 4 87 2 91 3 6
1 3 25 6 47 9 8
9 7 61 3 82 4 5
3 7 28 1 46 9 5
6 8 92 5 34 1 7
5 1 47 6 93 8 2


a well constructed su doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). the complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.
the 6k text file, sudoku.txt (right click and 'save link/target as...'), contains fifty different su doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).
by solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""