"""
The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.


if we then add a second layer to this solid it would require forty-six cubes to cover every visible face, the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.
however, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.
we shall define c(n) to represent the number of cuboids that contain n cubes in one of its layers. so c(22) = 2, c(46) = 4, c(78) = 5, and c(118) = 8.
it turns out that 154 is the least value of n for which c(n) = 10.
find the least value of n for which c(n) = 1000.
"""