class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def dfs(nums, start, val, sup):
            if val == 0 and sup == 0:
                ans.append(nums)
                return
            if val == 0 or sup == 0:
                return
            for i in range(start, 10):
                dfs(nums+[i], i+1, val-i, sup-1)
    
        dfs([], 1, n, k)
        return ans
                