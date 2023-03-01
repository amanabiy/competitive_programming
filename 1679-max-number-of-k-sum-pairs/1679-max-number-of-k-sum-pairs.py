class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        count = Counter()
        
        for i in range(len(nums)):
            count[nums[i]] += 1
            if i == len(nums) - 1 or nums[i + 1] != nums[i]:
                if k - nums[i] == nums[i]:
                    ans += count[nums[i]] // 2
                else:
                    ans += min(count[k - nums[i]], count[nums[i]])
        
        return ans