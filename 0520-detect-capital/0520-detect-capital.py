class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        numberCapital = 0
        numberSmall = 0
        n = len(word)
        
        for w in word:
            if w.islower():
                numberSmall += 1
            if w.isupper():
                numberCapital += 1
        
        if numberCapital == n or numberSmall == n:
            return True
        
        if numberCapital == 1 and word[0].isupper():
            return True
        
        return False