class Solution:
    def longestPrefix(self, s: str) -> str:
        if not s:
            return 0

        lps = [0] * len(s)
        prevLps = 0
        right = 1
        
        while right < len(s):
            # if the two letters are equal
            if s[right] == s[prevLps]:
                lps[right] = prevLps + 1
                right += 1
                prevLps += 1    
            elif prevLps == 0:
                right += 1
            else:
                prevLps = lps[prevLps - 1]
                
        return s[:lps[-1]]