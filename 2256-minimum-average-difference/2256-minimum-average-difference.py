class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        preSum = [0]
        minn = inf
        index = 0
        
        for i in nums:
            preSum.append(preSum[-1] + i)
        
        for i in range(1, len(preSum)):
            ans = ((preSum[i]) // i)
            if i < len(preSum) - 1:
                ans -= (preSum[-1] - preSum[i])//(len(nums) - i)
            if abs(ans) < minn:
                minn = abs(ans)
                index = i - 1
        
        return index