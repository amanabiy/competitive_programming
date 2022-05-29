class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        using the bits as a on off signal to know if the letter is present or not
        """
        letters = []
        ans = 0
        
        for word in words:
            temp = 0
            for ch in word:
                temp |= 1 << (ord(ch) - ord('a'))
            letters.append(temp)
        
        for i in range(len(words)):
            for j in range(len(words)):
                if letters[i] & letters[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
