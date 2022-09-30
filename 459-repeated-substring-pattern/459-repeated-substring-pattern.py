class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        abcabcabc
        
        """
        
        for i in range(len(s)//2):
            n = i + 1
            times = len(s) // n
            if s[:n] * times == s:
                # print(s[:n] * times == s, s[:n], s[:n] * times)
                return True
        
        return False