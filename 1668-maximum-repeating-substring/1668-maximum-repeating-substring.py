class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        
        for i in range(len(sequence)):
            for j in range(i, len(sequence) + 1, len(word)):
                size = (j - i) // len(word) 
                if sequence[i:j] == word * size:
                    ans = max(ans, size)

        return ans