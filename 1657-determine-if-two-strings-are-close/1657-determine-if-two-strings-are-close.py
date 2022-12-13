class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
         word1 = "aabbbc",
         word2 = "abbccc"
         do I have the same letters and the same frequency
        """
        c1 = Counter(word1)
        c2 = Counter(word2)

        for s in word1:
            if s not in c2:
                return False
        
        return sorted(c1.values()) == sorted(c2.values())