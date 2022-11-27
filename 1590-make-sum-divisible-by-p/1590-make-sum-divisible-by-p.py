class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        nums = [3,1,4,2], 
           p = 6
        (total - (s[i] - s[j])) % p = 0
        total % p - s[i] % p + s[j] % p = 0
        s[i] % p = total % p + s[j] % p -> this current index modulo
        total - (target) -> target
        s[j] % p = total % p - s[i] % p -> the prev index modulo so if I find this i can remove starting from here
        """
        toRemove = sum(nums) % p
        count = {0: -1}
        ans = float('inf')
        prefixSum = 0

        if toRemove == 0:
            return 0

        for i, num in enumerate(nums):
            prefixSum += num
            prev = (prefixSum % p - toRemove) % p
            rem = prefixSum % p
            if prev in count:
                ans = min(ans, i - count[prev])
            count[rem] = i

        return ans if ans != len(nums) else -1 