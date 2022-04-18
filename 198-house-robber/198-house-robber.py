class Solution:
    def rob(self, nums: List[int]) -> int:
        not_take = 0
        take = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            take, not_take = max(not_take + nums[i], take), take
        return max(take, not_take)