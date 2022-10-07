class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        taken = []
        
        def dfs(index, collected, sums):
            if sums == target:
                ans.append(collected[::])
                # taken.append(Counter(collected[::]))
                return
            
            for i in range(index, len(candidates)):
                if sums + candidates[i] <= target:
                    collected.append(candidates[i])
                    dfs(i, collected, sums + candidates[i])
                    collected.pop()
        
        dfs(0, [], 0)
        return ans
            
        