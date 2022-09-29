class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        
        """
        
        prefixSum = 0
        left = ans = 0
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            
            while prefixSum < i - left:
                prefixSum -= nums[left]
                left += 1
        
            ans = max(ans, i - left)
        
        return ans