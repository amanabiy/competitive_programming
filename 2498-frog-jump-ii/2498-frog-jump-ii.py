class Solution:
    def maxJump(self, stones: List[int]) -> int:
        """
        stones = [0,2,5,6,7]
                 [0,1,5,10]
        0 - 7 -> 7
        
        """
        forward = False
        backWard = False
        ans = float('-inf')
        
        for i in range(len(stones) - 2):
            v = abs(stones[i + 2] - stones[i])
            v2 = abs(stones[i] - stones[i + 1])
            ans = max(ans, v, v2)
        
        return ans if ans != float('-inf') else stones[-1]