"""
Nn disks are placed on a square game board. each disk has a black side and white side.

at each turn, you may choose a disk and flip all the disks in the same row and the same column as this disk: thus 2n-1 disks are flipped. the game ends when all disks show their white side. the following example shows a game on a 55 board.



it can be proven that 3 is the minimal number of turns to finish this game.

the bottom left disk on the nn board has coordinates (0,0);
the bottom right disk has coordinates (n-1,0) and the top left disk has coordinates (0,n-1). 

let cn be the following configuration of a board with nn disks:
a disk at (x,y) satisfying , shows its black side; otherwise, it shows its white side. c5 is shown above.

let t(n) be the minimal number of turns to finish a game starting from configuration cn or 0 if configuration cn is unsolvable.
we have shown that t(5)=3. you are also given that t(10)=29 and t(1 000)=395253.

find .
"""