class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        """
        target = 22
        nums = [2,7,11,15]
        dictionary = {
            20: 0,
            15: 1,
            11: 2,
            
            
        }
        """
        """
        Time: O(n)
        Space: O(n)
        """
        
        sumData = {}
        
        for i, n in enumerate(num):
            if n in sumData:
                return [i, sumData[n]]
            sumData[target - n] = i
        
        return [-1, -1]