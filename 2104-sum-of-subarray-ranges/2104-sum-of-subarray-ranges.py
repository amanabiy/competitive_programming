class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        [1, 2 ,3]
        """
        currMax, currMin = -inf, inf
        ans = 0

        for i in range(len(nums)):
            currMax, currMin = nums[i], nums[i]
            for j in range(i + 1, len(nums)):
                currMax = max(currMax, nums[j])
                currMin = min(currMin, nums[j])
                ans += (currMax - currMin)

        return ans