class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        right = 0
        long_sub = 0
        
        while right < len(s):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            right += 1
            long_sub = max(right - left, long_sub)

        return long_sub
                