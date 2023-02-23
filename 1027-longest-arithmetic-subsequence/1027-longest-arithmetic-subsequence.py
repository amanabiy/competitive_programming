class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = 1
        
        for i in range(-500, 500):
            lastNum = Counter()
            for j in nums:
                lastNum[j] = lastNum[j - i] + 1
                ans = max(ans, lastNum[j])
        
        return ans
                