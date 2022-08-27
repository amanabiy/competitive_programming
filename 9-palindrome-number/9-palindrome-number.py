class Solution:
    def isPalindrome(self, x: int) -> bool:
        return list(reversed(list(str(x)))) == list(str(x))