class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        [0,1,3,5,6,8,12,17]
                         |
        k = 5
        so at each position I can jump k, k + 1, k - 1
        at the begining my k is 1
        
        
        """
        if stones[1] != 1:
            return False

        reachedWithK = defaultdict(set)
        reachedWithK[1] = {1}
        
        for i in range(1, len(stones)):
            for j in reachedWithK[stones[i]]:
                val = stones[i] + j
                reachedWithK[val].add(j)
                reachedWithK[val + 1].add(j + 1)
                if j - 1 > 0:
                    reachedWithK[val - 1].add(j - 1)

        return len(reachedWithK[stones[-1]]) > 0 
        
            
            