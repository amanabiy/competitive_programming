class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        ans = float('inf')
        
        for i, val in enumerate(nums):
            if val not in count:
                count[val] = [1, i, i]
            else:
                count[val][0] += 1
                count[val][2] = i
        
        maxDist = max([c for c, _, _ in count.values()])
        for num in count:
            n, start, end = count[num]
            if n == maxDist:
                ans = min(end - start + 1, ans)
        
        return ans