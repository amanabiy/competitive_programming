class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            1, 5, 11, 5
        
        """
        allSum = sum(nums)
        nums.sort(reverse=True)
        def dfs(i, target, memo):
            
            if target == 0:
                return True
            
            if i >= len(nums):
                return False

            if (i, target) in memo:
                return memo[(i, target)]
            
            # take this element
            res = dfs(i + 1, target - nums[i], memo)
            
            if res:
                memo[(i, target)] = True
                return True

            # not take this element
            not_take = dfs(i + 1, target, memo)
            memo[(i, target)] = not_take

            return memo[(i, target)]

        
        if allSum % 2 == 1:
            return False
        # print(allSum)
        return dfs(0, allSum // 2, {0: True})