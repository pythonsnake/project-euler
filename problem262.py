"""
The following equation represents the continuous topography of a mountainous region, giving the elevation h at any point (x,y):




a mosquito intends to fly from a(200,200) to b(1400,1400), without leaving the area given by 0 ≤ x, y ≤ 1600.

because of the intervening mountains, it first rises straight up to a point a', having elevation f. then, while remaining at the same elevation f, it flies around any obstacles until it arrives at a point b' directly above b.

first, determine fmin which is the minimum constant elevation allowing such a trip from a to b, while remaining in the specified area.
then, find the length of the shortest path between a' and b', while flying at that constant elevation fmin.

give that length as your answer, rounded to three decimal places.

note: for convenience, the elevation function shown above is repeated below, in a form suitable for most programming languages:
h=( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )
"""