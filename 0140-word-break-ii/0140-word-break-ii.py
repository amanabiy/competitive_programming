class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = [ set() for _ in range(len(s))]
        
        def dfs(i, s, wordDict):
            if i >= len(s):
                return {''}

            if memo[i]:
                return memo[i]
        
            for j in range(i+1, i+11):
                word = s[i:j]
                if word in wordDict:
                    got = dfs(j, s, wordDict)
                    for sf in got:
                        split = " " if sf else ""
                        memo[i].add(word + split + sf)
            
            return memo[i]
        
        return dfs(0, s, set(wordDict))
        

            