"""
You probably know the game fifteen puzzle. here, instead of numbered tiles, we have seven red tiles and eight blue tiles.
a move is denoted by the uppercase initial of the direction (left, right, up, down) in which the tile is slid, e.g. starting from configuration (s), by the sequence lulur we reach the configuration (e):

(s), (e)


for each path, its checksum is calculated by (pseudocode):

checksum = 0
checksum = (checksum  243 + m1) mod 100 000 007
checksum = (checksum  243 + m2) mod 100 000 007
   …
checksum = (checksum  243 + mn) mod 100 000 007
where mk is the ascii value of the kth letter in the move sequence and the ascii values for the moves are:


l76r82u85d68

for the sequence lulur given above, the checksum would be 19761398.
now, starting from configuration (s),
find all shortest ways to reach configuration (t).

(s), (t)


what is the sum of all checksums for the paths having the minimal length?
"""