class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        sums = score =  0
        left = right = 0
        visited = set()
        
        while right < len(nums):
            if nums[right] in visited:
                visited.remove(nums[left])
                sums -= nums[left]
                left += 1
            else:
                visited.add(nums[right])
                sums += nums[right]
                right += 1
            
            score = max(score, sums)
            
            
        return score