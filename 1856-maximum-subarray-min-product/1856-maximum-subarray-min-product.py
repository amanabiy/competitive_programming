class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        """
        [1, 2, 3, 2]
        [1, 2, 2]
        """
        prefixSum = [0]
        stack = []
        ans = 0

        for i in nums:
            prefixSum.append(prefixSum[-1] + i)

        
        for i in range(len(nums)):
            # this means the number at the top can't be expanded no more
            # and this is the largest sub array that the num[i] can be large at
            newStart = i
            mod = 10 ** 9 + 7
            while stack and stack[-1][1] > nums[i]:
                start, val = stack.pop()
                maxSum = prefixSum[i] - prefixSum[start]
                ans = max(ans, maxSum * val)
                newStart = start
            
            stack.append([newStart, nums[i]])

        while stack:
            start, val = stack.pop()
            maxSum = prefixSum[-1] - prefixSum[start]
            ans = max(ans, maxSum * val)
        
        return ans % mod