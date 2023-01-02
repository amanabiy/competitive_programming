class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        s = s.split()
        m = len(s)

        if n != m:
            return False

        letterWord = {}
        wl = {}
        
        for i in range(n):
            if pattern[i] not in letterWord and s[i] not in wl:
                letterWord[pattern[i]] = s[i]
                wl[s[i]] = pattern[i]
            else:
                if pattern[i] in letterWord and letterWord[pattern[i]] != s[i]:
                    return False
                if s[i] in wl and wl[s[i]] != pattern[i]:
                    return False
        return True