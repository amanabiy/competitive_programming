class Solution:
    def findMostLeftPosition(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = -1 # it means it is the last element
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        longestSubsequence = [nums[0]]
        
        for i in range(1, len(nums)):
            val = self.findMostLeftPosition(longestSubsequence, nums[i])
            if val != -1:
                longestSubsequence[val] = nums[i]
            else:
                longestSubsequence.append(nums[i])
        
        return len(longestSubsequence)