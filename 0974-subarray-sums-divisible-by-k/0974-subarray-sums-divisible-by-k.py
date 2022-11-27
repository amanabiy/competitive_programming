class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        count = defaultdict(int)
        count[0] = 1
        prefixSum = 0
        
        for num in nums:
            prefixSum += num
            if prefixSum % k in count:
                ans += count[prefixSum % k]
            count[prefixSum % k] += 1
        
        return ans