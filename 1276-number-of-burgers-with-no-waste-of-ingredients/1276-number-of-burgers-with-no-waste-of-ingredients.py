class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        
        """
        16      7 
        12      6
        4 * 1 + 2 * 6 ->
        16 / 4
        """
        
        smallBurger  = (4*cheeseSlices - tomatoSlices)/2
        
        if smallBurger != int(smallBurger):
            return []
        
        jumboBurger = cheeseSlices - smallBurger
        if smallBurger < 0 or jumboBurger < 0:
            return []
        return [int(jumboBurger), int(smallBurger)]
        
        
        
        for one_cut in range(cheeseSlices//2+1):
            jb = one_cut
            sb = cheeseSlices - one_cut
            
            remaining = tomatoSlices -  (4 * jb)
            if (remaining / 2) == sb:
                return [jb, sb]
            
            sb, jb = jb, sb
            remaining = tomatoSlices -  (4 * jb)
            if (remaining / 2) == sb:
                return [jb, sb]
            
        return []
            # print(jb, sb)