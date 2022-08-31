class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
        4 2 5 3
              |
        2 4 3 5
              |
        even = 2 + 3
        odd = 4
        ans = 2 max(even, odd, ans, arr[i])
        """
        memo = {}
        def dfs(i, choosen):
            if (i, choosen) in memo:
                return memo[(i, choosen)]
            if i >= len(nums):
                return 0
            
            ans = nums[i] if choosen else -nums[i]
            
            # if choosen
            choose = ans + dfs(i + 1, not choosen)
            
            # if not choosedn
            not_choosen = dfs(i + 1, choosen)
            
            memo[(i, choosen)] = max(choose, not_choosen)
            return memo[(i, choosen)]
        
        return dfs(0, True)