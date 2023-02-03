class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        ans = True
        
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        
        if left < right:
            x = s[:left] + s[left+1:] == (s[:left] + s[left+1:])[::-1]
            y = s[:right] + s[right+1:] == (s[:right] + s[right+1:])[::-1]
            ans = x or y
        
        return ans