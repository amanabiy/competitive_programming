class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(num, collected):
            
            nonlocal k, n

            if len(collected) == k:
                ans.append(collected)
            
            elif num > 0 and len(collected) < k:
                for i in range(num, 0, -1):
                    collected.append(i)
                    dfs(i-1, collected[::])
                    collected.pop()

        dfs(n, [])
        
        return ans
            