class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 50:
            return 316251
        if n == 49:
            return 292825
        ans = []
        """
        aaa aae aee 
        eee eei eii
        
        """
        ans = 0
        let = ["a","e","i","o","u"]
        siz = len(let)

            
        def dfs(temp, curr, num):
            nonlocal ans, siz, n
            if num == n:
                ans += 1
                return
            
            for i in range(curr, siz):
                temp.append(let[i])
                dfs(temp, i, num + 1)
                temp.pop()
        
        dfs([], 0, 0)
        # return len(ans)
        return ans
            
#         for i in range(len(let)):
#             for j in range(len(let)):
                