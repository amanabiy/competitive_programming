class Solution:
    def rob(self, nums: List[int]) -> int:
        not_take = 0
        take = 0
        for i in range(len(nums)):
            take, not_take = max(not_take + nums[i], take), take
            
        return max(take, not_take)