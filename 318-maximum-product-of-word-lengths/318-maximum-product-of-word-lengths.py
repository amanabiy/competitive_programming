class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        
        """
        word = {}
        for i in range(len(words)):
            word[i] = set(list(words[i]))
        ans = 0
        for i in range(len(words)):
            for j in range(len(words)):
                intersect = word[i].intersection(word[j])
                if not intersect:
                    ans = max(len(words[i]) * len(words[j]), ans)
    
        return ans