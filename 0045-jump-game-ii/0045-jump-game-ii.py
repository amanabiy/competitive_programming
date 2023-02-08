class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReachable = [float('inf')] * len(nums)
        maxReachable[0] = 0
        
        for i, n in enumerate(nums):
            if maxReachable[i] != float('inf'):
                for j in range(i, min(i + n + 1, len(nums))):
                    maxReachable[j] = min(maxReachable[j], maxReachable[i] + 1)
        
        return maxReachable[-1]