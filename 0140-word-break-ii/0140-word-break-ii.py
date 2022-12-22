class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = [ set() for _ in range(len(s))]
        n = len(s)
        
        def dfs(i, s, wordDict, n):
            if i >= len(s):
                return {''}

            if memo[i]:
                return memo[i]

            size = min(i+11, n+1)
            for j in range(i+1, size):
                word = s[i:j]
                if word in wordDict:
                    got = dfs(j, s, wordDict, n)
                    for sf in got:
                        split = " " if sf else ""
                        memo[i].add(word + split + sf)
            
            return memo[i]
        
        return dfs(0, s, set(wordDict), n)
        

            