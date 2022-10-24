class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        nums = [2, 2, 3, 3, 3, 4]
        If I take 2 -> I can't take 3 and 4
        if I take 3 -> I can't take 2 and 4
        If I take 4 -> I can't take 4 and 5 (if there is)
        2 it self -> 
        3 it self or 2 
        4 it self + 2 or 3 (total until now)
        """
        count = Counter(nums)
        nums = sorted(count.keys())
        dp = [ 0 for _ in range(len(nums) + 2) ]
        
        # print(dp)
        for i in range(2, len(dp)):
            if i - 3 >= 0 and nums[i - 3] == nums[i - 2] - 1:
                dp[i] = max((count[nums[i - 2]] * nums[i - 2]) + dp[i - 2], dp[i - 1])
            else:
                dp[i] = (count[nums[i - 2]] * nums[i - 2]) + dp[i - 1]
        
        
        # print(dp)
        return dp[-1]