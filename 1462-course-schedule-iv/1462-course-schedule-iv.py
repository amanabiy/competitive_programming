class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [ [ False for _ in range(n) ] for _ in range(n) ]
        ans = []
        
        # build graph
        for pre, dst in prerequisites:
            dp[pre][dst] = True
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])
        
        for fr, to in queries:
            ans.append(dp[fr][to])
        
        return ans