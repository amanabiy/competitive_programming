class Solution:
    def checkPalindrome(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

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
            x = self.checkPalindrome(s[:left] + s[left+1:])
            y = self.checkPalindrome(s[:right] + s[right+1:])
            ans = x or y
        
        return ans