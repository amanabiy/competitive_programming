class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        """
        text = "abdcdbc",
        pattern = "ac"
        
        aacbdcdbc
        
        ac ac ac ac ac ac
        
        """
        
        ca = 0
        madePatterns = 0
        cb = 0        
        for l in text:
            if l == pattern[1]:
                cb += 1
                madePatterns += ca
            if l == pattern[0]:
                ca += 1

        
        if ca > cb:
            return madePatterns + ca
        return madePatterns + cb
        