class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = [-inf] * len(nums)
        maxs[0] = nums[0]
        
        for i in range(1, len(nums)):
            maxs[i] = max(nums[i], maxs[i - 1] + nums[i])
        # print (maxs)
        return max(maxs)