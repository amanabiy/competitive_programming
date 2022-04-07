class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1:
            return ""

        left = 0
        replaced = 0
        letter = 'a'
        
        while left < len(palindrome) // 2 or replaced == 0:
            if replaced == 0 and left == len(palindrome) // 2:
                left = 0
                letter = chr(ord(letter) + 1)
            if palindrome[left] < letter:
                palindrome = palindrome[: len(palindrome) - left - 1] + letter + \
                             palindrome[len(palindrome) - left:]
                break
            if palindrome[left] != letter:
                palindrome = palindrome[:left] + letter + palindrome[left+1:]
                break
            left += 1
        
        return palindrome
            