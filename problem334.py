"""
In plato's heaven, there exist an infinite number of bowls in a straight line.
each bowl either contains some or none of a finite number of beans.
a child plays a game, which allows only one kind of move: removing two beans from any bowl, and putting one in each of the two adjacent bowls. the game ends when each bowl contains either one or no beans.

for example, consider two adjacent bowls containing 2 and 3 beans respectively, all other bowls being empty. the following eight moves will finish the game:



you are given the following sequences:
      t0 = 123456.
   

      ti = 
   
   
   
   
      
         ti-12
      
         ,
      
      
      
         if ti-1 is even
      
      
      
         ti-12
      
         
      
         926252, 
      
      
         if ti-1 is odd
      
      

   
   
      where x is the floor function
   

   
   
      and  is the bitwise xor operator.
   

      bi = ( ti mod 211) + 1.
   
the first two terms of the last sequence are b1 = 289 and b2 = 145.
if we start with b1 and b2 beans in two adjacent bowls, 3419100 moves would be required to finish the game.

consider now 1500 adjacent bowls containing b1, b2,..., b1500 beans respectively, all other bowls being empty. find how many moves it takes before the game ends.
"""