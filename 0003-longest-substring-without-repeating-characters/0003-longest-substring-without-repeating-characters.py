class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        ans = 0

        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[i])
            ans = max(ans, i - left + 1)
        
        return ans