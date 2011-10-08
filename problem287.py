"""
The quadtree encoding allows us to describe a 2n2n  black and white image as a sequence of bits (0 and 1). those sequences are to be read from left to right like this:
the first bit deals with the complete 2n2n region;
"0" denotes a split:
the current 2n2n region is divided into 4 sub-regions of dimension 2n-12n-1,
the next bits contains the description of the top left, top right, bottom left and bottom right sub-regions - in that order;
"10" indicates that the current region contains only black pixels;
"11" indicates that the current region contains only white pixels.consider the following 44 image (colored marks denote places where a split can occur):

this image can be described by several sequences, for example :
"001010101001011111011010101010", of length 30, or
"0100101111101110", of length 16, which is the minimal sequence for this image.

for a positive integer n, define dn as the 2n2n image with the following coloring scheme:
the pixel with coordinates x = 0, y = 0 corresponds to the bottom left pixel,
if (x - 2n-1)2 + (y - 2n-1)2  22n-2 then the pixel is black,
otherwise the pixel is white.what is the length of the minimal sequence describing d24 ?
"""