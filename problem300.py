"""
In a very simplified form, we can consider proteins as strings consisting of hydrophobic (h) and polar (p) elements, e.g. hhpphhhphhph. 
for this problem, the orientation of a protein is important; e.g. hpp is considered distinct from pph. thus, there are 2n distinct proteins consisting of n elements.

when one encounters these strings in nature, they are always folded in such a way that the number of h-h contact points is as large as possible, since this is energetically advantageous.
as a result, the h-elements tend to accumulate in the inner part, with the p-elements on the outside.
natural proteins are folded in three dimensions of course, but we will only consider protein folding in two dimensions.

the figure below shows two possible ways that our example protein could be folded (h-h contact points are shown with red dots).



the folding on the left has only six h-h contact points, thus it would never occur naturally.
on the other hand, the folding on the right has nine h-h contact points, which is optimal for this string.

assuming that h and p elements are equally likely to occur in any position along the string, the average number of h-h contact points in an optimal folding of a random protein string of length 8 turns out to be 850 / 28=3.3203125.

what is the average number of h-h contact points in an optimal folding of a random protein string of length 15?
give your answer using as many decimal places as necessary for an exact result.
"""