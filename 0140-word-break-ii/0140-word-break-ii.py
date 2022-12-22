class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = set()
        
        def backtrack(i, collected, s, wordDict):
            if i >= len(s):
                # add it to your answer
                ans.add(' '.join(collected))
            
            for j in range(i, i + 11):
                if s[i:j] in wordDict:
                    collected.append(s[i:j])
                    backtrack(j, collected, s, wordDict)
                    collected.pop()
        
        backtrack(0, [], s, set(wordDict))
        return ans
                    
            