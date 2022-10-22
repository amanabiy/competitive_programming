class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        take = 0
        not_take = 0
        n = len(nums)
        ans = 0
    
        for i in range(n - 1):
            take, not_take = max(take, not_take + nums[i]), take
        
        print(ans, take, not_take)
        ans = max(take, not_take)

        take = not_take = 0
        for i in range(1, n):
            take, not_take = max(take, not_take + nums[i]), take
        
        ans = max([ans, take, not_take])
        return ans
            