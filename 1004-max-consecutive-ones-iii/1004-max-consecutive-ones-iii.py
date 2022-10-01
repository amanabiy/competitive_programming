class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        collected = 0
        left = 0
        ans = 0
        
        for i in range(len(nums)):
            collected += nums[i]
    
            while collected + k < (i - left + 1):
                collected -= nums[left]
                left += 1
    
            ans = max(ans, i - left + 1)
        
        return ans