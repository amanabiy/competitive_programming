class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """
        Time: O(n)
        Space: O(n + 26)
        """
        
        letters = defaultdict(int)
        found = 0
        
        for i in range(len(p)):
            if i > 0 and chr(ord(p[i - 1]) + 1) == p[i] or (p[i - 1] == 'z' and p[i] == 'a'):
                found += 1
            else:
                found = 1
            letters[p[i]] = max(letters[p[i]], found)
        
        return sum(letters.values())