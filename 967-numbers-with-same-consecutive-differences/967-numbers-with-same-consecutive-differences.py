class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        """
        181
        
        """
        ans = []
        
        def dfs(i, collected):
            if len(collected) == n:
                ans.append(collected[::])
                return
            
            for j in range(10):
                if (collected and abs(collected[-1] - j) == k) or (j != 0 and not collected):
                    collected.append(j)
                    dfs(j, collected)
                    collected.pop()

        dfs(0, [])
        for i in range(len(ans)):
            ans[i] = ''.join(list(map(str, (ans[i]))))

        return ans