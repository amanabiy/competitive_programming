class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        """
        target = 22
        nums = [2,7,11,15]
        Time: (n^2)
        space: O(1)
        
        """
        
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[i] + num[j] == target:
                    return [i, j]
                
        return [-1, -1]