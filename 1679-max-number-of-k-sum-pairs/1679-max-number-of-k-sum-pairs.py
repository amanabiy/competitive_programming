class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter()
        
        for i in range(len(nums)):
            diff = k - nums[i]
            if count[diff]:
                ans += 1
                count[diff] -= 1
            else:
                count[nums[i]] += 1
                
        return ans