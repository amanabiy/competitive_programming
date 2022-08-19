class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]

        def pal(i, j):
            # left = i - 1
            # right = j + 1
            ans = 0

            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                ans += 1
                i -= 1
                j += 1
            return s[i+1:j]
        
        for i in range(len(s) - 1):
            one_center, two_center = pal(i, i), pal(i, i + 1)
            if len(one_center) > len(ans):
                ans = one_center
            if len(two_center) > len(ans):
                ans = two_center
        
        return ans
