class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        return the minimal length which has sum > or equal to target
        nums = [2,3,1,2,4,3]
                l
                  r
            currSum = 7
            minLength = 2
        """
        minLength = float('inf')
        currSum = 0
        left = 0
        
        for i in range(len(nums)):
            currSum += nums[i]
            
            while currSum >= target:
                minLength = min(i - left + 1, minLength)
                currSum -= nums[left]
                left += 1
        
        return minLength if minLength != inf else 0
        