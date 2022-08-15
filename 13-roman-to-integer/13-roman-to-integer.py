class Solution:
    def romanToInt(self, s: str) -> int:
        """
        4 + 90 + 900 + 1000
        1
        """
        romanNumber = {
            "I": 1, 
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        ans = 0
        
        for i in range(len(s) - 1, -1, -1):
            if i + 1 < len(s) and romanNumber[s[i+1]] > romanNumber[s[i]]:
                ans -= romanNumber[s[i]]
            else:
                ans += romanNumber[s[i]]

        return ans