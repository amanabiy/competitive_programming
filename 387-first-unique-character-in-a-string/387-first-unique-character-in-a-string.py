class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        count = Counter(s)
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                ans = i
                break
        
        return ans
        