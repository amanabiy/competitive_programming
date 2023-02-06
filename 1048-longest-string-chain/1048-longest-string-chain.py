class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)
        ans = [1] * n
        
        for i in range(n):
            seen = set()
            
            for i2 in range(len(words[i])):
                b = words[i][:i2] + words[i][i2+1:]
                if b != words[i]:
                    seen.add(b)
            
            for j in range(i):
                if words[j] in seen:
                    ans[i] = max(ans[i], 1 + ans[j])

        return max(ans)