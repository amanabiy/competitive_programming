class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums] 
        heapq.heapify(nums)
        score = 0

        while k and nums[0] != 1:
            x = heapq.heappop(nums) * - 1
            score += x
            heapq.heappush(nums, ceil(x / 3) * -1)
            k -= 1
        
        return score + k
        