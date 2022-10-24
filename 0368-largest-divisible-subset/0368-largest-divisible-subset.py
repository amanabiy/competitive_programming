class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,3] -> a % b == 0
                          b % a == 0
        for each element:
        I have two choices ->
            taking this element and the second one is not take it
            my next dividor is going to be this number
        """

        def dfs(i, prev = None, memo = {}):
            if i >= len(nums):
                return set()
            
            if (i, prev) in memo:
                return memo[(i, prev)]
    
            take = set()
            not_take = set()
            
            if not prev or (nums[i] % prev == 0):
                take =  set(dfs(i + 1, nums[i], memo))
                take.add(nums[i])
    
            not_take = dfs(i + 1, prev, memo)
            
            ans = None

            if len(take) > len(not_take):
                ans = take
            else:
                ans = not_take
            # print(nums[i], ans)
            memo[(i, prev)] = ans
            return ans

        nums.sort()        
        return dfs(0)
        