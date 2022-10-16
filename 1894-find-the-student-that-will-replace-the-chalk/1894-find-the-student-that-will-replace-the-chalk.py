class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """
        chalk = [5,1,5], k = 22
        22 % 11 -> 0
        [5]
        
        chalk = [3,4,1,2], k = 25
                   |
                 5 - 3 = 2
        25 % (10) -> 5
        """
        
        k = k % sum(chalk)
        
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        