class Solution:
    def buildPrefix(self, arr, letter):
        prefix = [0]
        
        for a in arr:
            val = prefix[-1]
            if a == letter:
                val += 1
            prefix.append(val)
        
        return prefix

    def minimumDeletions(self, s: str) -> int:
        forward = self.buildPrefix(s, 'b')
        backward = self.buildPrefix(s[::-1], 'a')[::-1]
        ans = float('inf')

        for i in range(len(s)):
            ans = min(ans, forward[i] + backward[i + 1])
        
        return ans

        
                