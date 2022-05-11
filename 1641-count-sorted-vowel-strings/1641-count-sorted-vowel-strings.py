class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = 0
        let = ["a","e","i","o","u"]
        siz = len(let)

            
        def dfs(curr, num):
            nonlocal ans, siz
            if num == 0:
                ans += 1
                return

            for i in range(curr, siz):
                dfs(i, num - 1)
        
        dfs( 0, n)
        return ans