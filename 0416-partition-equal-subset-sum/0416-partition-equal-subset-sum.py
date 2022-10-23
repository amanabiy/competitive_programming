class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            1, 5, 11, 5
        
        """
        l, s = len(nums), sum(nums)
        @cache  # this is important to avoid unnecessary recursion
        def dfs(curr: int, idx: int) -> bool:
            """
            Select elements and check if nums can be partitioned.
            :param curr: The current sum of the elements in the subset.
            :param idx: The index of the current element in nums.
            :return: True if nums can be partitioned, False otherwise.
            """
            if idx == l:  # we have reached the end of the array
                return curr == s>>1
            elif curr+nums[idx] == s>>1 or (curr+nums[idx] < s>>1 and dfs(curr+nums[idx], idx+1)):  # or, target sum will be reached by selecting this element
                return True
            return dfs(curr, idx+1)  # else, don't select this element, continue
        return False if s&1 else dfs(0, 0)