class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        a  b  a  b   c   bacadefegdehijhklij
        a  ab ab ab  abc
        abc
        defg
        hijkl
        
        
        """
        ans = []
        lastSeen = {}
        for i in range(len(s)):
            lastSeen[s[i]] = i
        
        left = 0
        right = 0
        while left < len(s):
            end = lastSeen[s[left]]
            while right <= end:
                end = max(lastSeen[s[right]], end)
                right += 1
            ans.append(right - left)
            left = right

        return ans