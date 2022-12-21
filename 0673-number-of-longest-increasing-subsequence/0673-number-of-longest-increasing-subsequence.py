class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        1
        """
        dp = [1] * len(nums)
        dpCount = [1] * len(nums)
        maxim = 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    newValue = dp[i] + 1
                    if newValue > dp[j]:
                        dp[j] = newValue
                        dpCount[j] = dpCount[i]
                    elif newValue == dp[j]:
                        dpCount[j] += dpCount[i]
                    maxim = max(dp[j], maxim)

        ans = 0
        for i in range(len(nums)):
            if dp[i] == maxim:
                ans += dpCount[i]

        return ans
        