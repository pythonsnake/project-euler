"""
A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special colour-proofing paper of size a5.
every monday morning, the foreman opens a new envelope, containing a large sheet of the special paper with size a1.
he proceeds to cut it in half, thus getting two sheets of size a2. then he cuts one of them in half to get two sheets of size a3 and so on until he obtains the a5-size sheet needed for the first batch of the week.
all the unused sheets are placed back in the envelope.

at the beginning of each subsequent batch, he takes from the envelope one sheet of paper at random. if it is of size a5, he uses it. if it is larger, he repeats the 'cut-in-half' procedure until he has what he needs and any remaining sheets are always placed back in the envelope.
excluding the first and last batch of the week, find the expected number of times (during each week) that the foreman finds a single sheet of paper in the envelope.
give your answer rounded to six decimal places using the format x.xxxxxx .
"""