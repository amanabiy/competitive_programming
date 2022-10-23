class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            1, 5, 11, 5
        
        """
        totalSum = sum(nums)
        
        if totalSum % 2 == 1:
            return False
        seen = set([0])        
        half =  totalSum // 2

        for num in nums:
            collect = []
            for x in seen:
                if x + num == half:
                    return True
                collect.append(x + num)
            seen = seen | set(collect)

        return False