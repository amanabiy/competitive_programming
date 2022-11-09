class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        """
        letters = []
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        ans = []
        strs = list(s)
        
        for i in range(len(s)):
            if s[i] not in digits:
                letters.append(i)
        
        for i in range(1 << len(letters)):
            text = strs
            index = 0
            while index <= len(letters) - 1:
                mask = i & (1 << index)
                if mask:
                    text[letters[index]] = s[letters[index]].upper()
                else:
                    text[letters[index]] = s[letters[index]].lower()
                index += 1
            ans.append(''.join(text))

        return ans
        
                