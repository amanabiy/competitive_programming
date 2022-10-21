class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastSeen = {}
        ans = False
        
        for i in range(len(nums)):
            if nums[i] in lastSeen:
                ans = ans or abs(i - lastSeen[nums[i]]) <= k
            lastSeen[nums[i]] = i

        return ans